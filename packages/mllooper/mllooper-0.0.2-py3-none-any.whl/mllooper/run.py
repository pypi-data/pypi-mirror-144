import importlib
import json
import re
import subprocess
import sys
from importlib.util import spec_from_file_location, module_from_spec, find_spec
from pathlib import Path
from typing import Tuple

import click
from click import BadParameter
from pydantic import ValidationError
from yaloader import ConfigLoader
from yaml import MarkedYAMLError

from mllooper import Module, ModuleConfig


def install_package(package_name: str):
    try:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--force-reinstall', package_name])
    except subprocess.CalledProcessError as e:
        raise RuntimeError(f"Could not install {package_name}")


def is_valid_module_name(module_name: str):
    pattern = r"^[a-zA-Z_][a-zA-Z0-9_]*$"
    return re.fullmatch(pattern, module_name)


def import_as_known_module(module_name: str):
    if not is_valid_module_name(module_name):
        raise ModuleNotFoundError
    importlib.import_module(module_name)


def import_from_disk(module_name: str):
    module_path = Path(module_name).absolute()
    if module_path.is_file() and module_path.suffix == '.py':
        name = module_path.parent.name
        location = module_path
    elif module_path.is_dir() and module_path.joinpath('__init__.py').is_file():
        name = module_path.name
        location = module_path.joinpath('__init__.py')
    else:
        raise ModuleNotFoundError

    if find_spec(name) is not None:
        name = f"{name}_mllooper_auto_import"

    spec = spec_from_file_location(name, location)
    module = module_from_spec(spec)
    sys.modules[name] = module
    spec.loader.exec_module(module)


def import_module(module_name: str):
    # try to import as a known module
    try:
        import_as_known_module(module_name)
    except ModuleNotFoundError:
        pass
    else:
        return

    # try to import as file or directory
    try:
        import_from_disk(module_name)
    except ModuleNotFoundError:
        pass
    else:
        return

    raise ModuleNotFoundError(f"Could not import {module_name}")


@click.group()
def cli():
    pass


@cli.command()
@click.option("-c", "--config", "config_paths", multiple=True, default=[], type=Path)
@click.option("-d", "--dir", "config_dirs", multiple=True, default=[], type=Path)
@click.option("-y", "--yaml", "yaml_strings", multiple=True, default=[], type=str)
@click.option("-i", "--install", "install_packages", multiple=True, default=[])
@click.option("-i", "--import", "import_modules", multiple=True, default=[])
@click.option("--autoload/--no-autoload", "auto_load", default=False)
@click.argument('run_config', type=str)
def run(config_paths: Tuple[Path], config_dirs: Tuple[Path], yaml_strings: Tuple[str],
        install_packages: Tuple[str], import_modules: Tuple[str], run_config: str, auto_load: bool):

    # install packages before importing modules
    for package in install_packages:
        try:
            install_package(package)
        except RuntimeError as e:
            raise BadParameter(f"{e}") from e

    # import modules before creating the loader
    for module in import_modules:
        try:
            import_module(module)
        except ModuleNotFoundError as e:
            raise BadParameter(f"{e}") from e

    config_loader = ConfigLoader()

    # add configurations
    for config_dir in config_dirs:
        try:
            config_loader.load_directory(config_dir.absolute())
        except (NotADirectoryError, MarkedYAMLError, ValidationError) as e:
            raise BadParameter(f"{e}") from e

    for config_path in config_paths:
        try:
            config_loader.load_file(config_path.absolute())
        except (FileNotFoundError, MarkedYAMLError, ValidationError) as e:
            raise BadParameter(f"{e}") from e

    for yaml_string in yaml_strings:
        try:
            config_loader.load_string(yaml_string)
        except (MarkedYAMLError, ValidationError) as e:
            raise BadParameter(f"{e}") from e

    # load and run the run configuration
    if (path := Path(run_config)).is_file():
        try:
            constructed_run = config_loader.construct_from_file(path, auto_load=auto_load)
        except (FileNotFoundError, MarkedYAMLError, ValidationError) as e:
            raise BadParameter(f"{e}") from e
    else:
        try:
            constructed_run = config_loader.construct_from_string(run_config, auto_load=auto_load)
        except (MarkedYAMLError, ValidationError) as e:
            raise BadParameter(f"{e}") from e

    if auto_load:
        if not isinstance(constructed_run, Module):
            raise BadParameter(f"The run configuration RUN_CONFIG has to be a mllooper Module."
                               f"Got {type(constructed_run)} instead.")
        constructed_run.run()
    else:
        if not isinstance(constructed_run, ModuleConfig):
            raise BadParameter(f"The run configuration RUN_CONFIG has to be a mllooper Module. "
                               f"Got {type(constructed_run)} instead.")
        constructed_run.load().run()


@cli.command()
@click.argument('tag', type=str)
@click.option("--definitions/--no-definitions", "definitions", default=False)
def info(tag: str, definitions: bool):
    config_loader = ConfigLoader()

    try:
        config = config_loader.yaml_loader.yaml_config_classes[tag]
    except KeyError:
        raise BadParameter(f"There is no configuration definition loaded for the tag {tag}. "
                           f"Make sure that the configuration class is imported.")

    jschema: str = config.schema_json(ref_template='/REPLACE/{model}/REPLACE/')

    for config_tag, config_class in config_loader.yaml_loader.yaml_config_classes.items():
        jschema = jschema.replace(f'"{config_class.__name__}": {{"title": "{config_class.__name__}"',
                                  f'"{config_tag}": {{"title": "{config_tag}"')
        jschema = jschema.replace(f'"title": "{config_class.__name__}"', f'"title": "{config_tag}"')
        jschema = jschema.replace(f'/REPLACE/{config_class.__name__}/REPLACE/', f'#/definitions/{config_tag}')

    # Replace definitions of models which are not configurations
    jschema = re.sub(r'/REPLACE/(?P<name>.*?)/REPLACE/', r'#/definitions/\g<name>', jschema)

    schema = json.loads(jschema)
    print(
        f"{schema['title']}\n{schema['description']}"
    )
    print(
        f"\n\nproperties: {json.dumps(schema['properties'], indent=2)}"
    )
    if definitions:
        print(
            f"\n\ndefinitions: {json.dumps(schema['definitions'], indent=2)}"
        )


if __name__ == '__main__':
    cli()
