install:
	poetry install

build:
	poetry build

package-install:
	python3 -m pip install --user dist/*.whl --no-warn-script-location