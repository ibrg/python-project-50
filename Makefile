install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --no-warn-script-location

lint: 
	python -m flake8 gendiff

test:
	poetry run pytest

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml