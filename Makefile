SHELL := /bin/bash

run:
	uvicorn sql_app.main:app --reload

test:
	python3 -m unittest sql_app.tests.unit_tests