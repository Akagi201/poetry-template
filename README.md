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
# run into env
poetry shell
python src/poetry_template/main.py
# or simpl
poetry run python src/poetry_template/main.py
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
