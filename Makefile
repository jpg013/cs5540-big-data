# Makfile for project

run:
	python stream.py

stream:
	python stream.py

test:
	python -m unittest discover -s ./tests -p '*_test.py'

install:
	pip install -r requirements.txt
