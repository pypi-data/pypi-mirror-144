from pathlib import Path

import typer

from aoricaan_cli.src.utils.debugger import Debug

work_path = Path('src/lambdas')

if not work_path.exists() and Path('./.env.dist').exists():
    Debug.error(f'The folder {work_path} does not exist!')
    raise typer.Abort()
