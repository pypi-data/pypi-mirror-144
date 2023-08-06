import os
from pathlib import Path

import typer

from aoricaan_cli import templates
from aoricaan_cli.src.utils.aws_templates_implementation import create_all_files_for_initial_project, force_lowercase
from aoricaan_cli.src.utils.debugger import Debug
from aoricaan_cli.src.utils.install_layers import install
from aoricaan_cli.src.utils.state import State
from aoricaan_cli.src.utils.synth import build_all_lambdas, update_deploy_id_resource_api_gateway, build_layers

state = State()
app = typer.Typer()


@app.command('synth')
def build_project():
    """
    Build the files for deploy the project in aws.
    """
    template_path = Path("templates/projectTemplate.json")
    lambdas_path = Path("src/lambdas")
    layers_path = Path("src/layers")
    api_path = Path("src/api.json")

    # TODO: Modify for use best practices.
    build_all_lambdas(lambdas_path=lambdas_path, path_cfn_template=template_path,
                      path_swagger_template=api_path, bucket=os.environ.get('artifact_bucket'))
    update_deploy_id_resource_api_gateway(path_template=template_path)
    build_layers(layers_path=layers_path)


@app.command('install')
def install_layers():
    """
    Install layer in local environment.
    """
    install()


@app.command('init')
def initialize_new_project(name: str = typer.Option(..., help='Name for this project',
                                                    callback=force_lowercase, prompt='Project name'),
                           artifacts_bucket: str = typer.Option(None,
                                                                help='Bucket name where all artifacts will be saved, '
                                                                     'if you pass phe option "use_pipeline" like true '
                                                                     'this option can be empty',
                                                                callback=force_lowercase,
                                                                prompt='Artifacts Bucket'),
                           environment: str = typer.Option('dev', help='Name for the environment',
                                                           callback=force_lowercase),
                           network_stack: str = typer.Option(None,
                                                             help='Stack with all networking definition deployed in '
                                                                  'the same account.'),
                           use_core_layers: bool = typer.Option(True,
                                                                help='Define of you like use the core layers in your '
                                                                     'project.'),
                           use_pipeline: bool = typer.Option(False,
                                                             help='Define true if you like implement a CD/CI '
                                                                  'implementation')):
    """
    Initialize a new empty project in the current path.

    """
    path = Path(os.getcwd())
    create_repo = False
    if use_pipeline:
        create_repo = typer.confirm('You wanna create a repo for this project?')
    if not create_repo and use_pipeline:
        repo_name = typer.prompt('Repository name')

    create_all_files_for_initial_project(project_name=name, artifact_bucket=artifacts_bucket)
    Debug.success('Project init successfully!')


@app.command('show')
def show_path():
    print(os.path.dirname(templates.__file__))


@app.callback()
def root(ctx: typer.Context, verbose: bool = False):
    """
    Manage the project.

    """
    state.verbose = verbose
    if state.verbose and ctx.invoked_subcommand:
        Debug.info(f"Running command: {ctx.invoked_subcommand}")


if __name__ == '__main__':
    app()
