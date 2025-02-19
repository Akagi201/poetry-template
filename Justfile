install:
  uv sync --all-extras

format:
  uv run ruff format .

fix:
  uv run ruff check . --fix

check:
  uv run ruff check .
