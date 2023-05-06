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
