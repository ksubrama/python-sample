.PHONY: init test run
.DEFAULT_GOAL := test

init:
	pip install -r requirements.txt

lint:
	flake8 .

test: lint
	python -m pytest

run:
	python app.py
