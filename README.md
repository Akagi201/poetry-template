# poetry template

## New project

poetry new

```sh
poetry new poetry-template --src --name=poetry-template
```

or poetry init inside a folder

```sh
poetry init
```

## Create .gitignore

```sh
curl -L https://www.toptal.com/developers/gitignore/api/python > .gitignore
```

## Poetry env

```sh
poetry env info
poetry install # install all dependencies in the virtualenv
poetry shell # spawn a shell within the virtual environment
poetry show # show all packages
poetry update # update all packages
python src/poetry_template/main.py
# or simpl
poetry run python src/poetry_template/main.py
poetry build # package the project
poetry publish # publish the project
```

## Add packages

```sh
poetry add <package>
poetry add ./lib/<package>
```

## Install dependencies

```sh
poetry install --with jupyterlab
poetry install --only main
```

## Jupyter

If use conda packages, use a separate venv in mini-conda

```sh
poetry run jupyter lab src/notebooks
```

## requirements.txt generation

```sh
poetry export --without-hashes --with dev --format=requirements.txt > requirements.txt
```

## Python Libs

* [dask](https://www.dask.org/) - Parallel computing
* [FFTW](https://doku.lrz.de/fftw-fastest-fourier-transform-in-the-west-11481674.html) - FFT Wrapper
* [httpx](https://github.com/encode/httpx) - next generation HTTP client lib and cli
* [aiohttp](https://github.com/aio-libs/aiohttp) - Asyncio http client/server
* [websockets](https://github.com/python-websockets/websockets) - websockets client and server library
* [aiogram](https://github.com/aiogram/aiogram) - Asyncio telegram bot framework
* [loguru](https://github.com/Delgan/loguru) - simple json logger
* [Typer](https://github.com/tiangolo/typer) - cli parser

## Python tools

* [mypy](https://mypy-lang.org/) - Static type checker
* [ruff](https://github.com/astral-sh/ruff) - Python linter and formatter
* [erg](https://github.com/erg-lang/erg) - Rust like lang can interop with python
* [pylyzer](https://github.com/mtshiba/pylyzer) - alternative to mypy
* [pixi](https://prefix.dev/) - conda dep manager tool
* [rvp](https://github.com/samgozman/rvp) - alternative to poetry
* [unpack](https://github.com/bnkc/unpack) - Unpack python packages

## Python Books

* [Python Design Patterns](https://python-patterns.guide/) - Python Design Patterns implementation of the [Gang of Four book](https://python-patterns.guide/gang-of-four/)
