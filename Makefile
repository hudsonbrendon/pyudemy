install:
	pipenv run python setup.py install

black:
	pipenv run black . --check

coverage:
	pipenv run coverage report -m

test:
	pipenv run python tests/tests.py

dev:
	make install
	make test