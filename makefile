.PHONY: help clean venv test lint format

VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

help:
	@echo "HEEEEEELP!"

venv/bin/activate: requirements.txt
	python3 -m venv $(VENV)
	$(PIP) install -r requirements.txt

clean:
	rm -rf $(VENV)
	find . -type f -name '*.pyc' -delete

venv: venv/bin/activate

lint: venv/bin/activate
	$(PYTHON) -m pylint --recursive=y . --ignore=venv

format: venv/bin/activate
	$(PYTHON) -m yapf -ir . --exclude venv --style='{column_limit: 120}'