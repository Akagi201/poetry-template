install:
  poetry install
  poetry run pip install --upgrade pip
  poetry run pip install -r requirements.txt

format:
  ruff format .

fix:
  ruff check . --fix

check:
  ruff format --check
  ruff check
