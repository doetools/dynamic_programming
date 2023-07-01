serve:
	poetry run python -m mkdocs serve

build:
	poetry run python -m mkdocs build

deploy:
	poetry run python -m mkdocs gh-deploy