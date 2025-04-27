SHELL := /bin/bash
PYTHON = python3
TEST_PATH = ./tests/
FLAKE8_EXCLUDE = venv,.venv,.eggs,.tox,.git,__pycache__,*.pyc


all: clean install-dev test

check:
	${PYTHON} -m flake8 . --count --select=E9,F63,F7,F82 --show-source --statistics --exclude ${FLAKE8_EXCLUDE}
	${PYTHON} -m flake8 . --count --exit-zero --max-complexity=10 --max-line-length=79 --statistics --exclude ${FLAKE8_EXCLUDE}

check-workflows:
	act -P ubuntu-latest=nektos/act-environments-ubuntu:18.04 -p

clean:
	@find . -name '*.pyc' -exec rm --force {} +
	@find . -name '*.pyo' -exec rm --force {} +
	@find . -name '*~' -exec rm --force {} +
	rm -rf build
	rm -rf dist
	rm -rf *.egg-info
	rm -f *.sqlite
	rm -rf .cache

dist: clean
	@python setup.py sdist bdist_wheel

deploy: dist
	@echo "-------------------- sending to testpypi server ------------------------"
	@twine upload -r testpypi dist/*

help:
	@echo "---------------------------- help --------------------------------------"
	@echo "    clean"
	@echo "        Remove python artifacts and build artifacts."
	@echo "    isort"
	@echo "			Sort import statements."
	@echo "    check"
	@echo "        Check style with flake8."
	@echo "    test"
	@echo "        Run pytest"
	@echo "    check-workflows"
	@echo "        Run act"

install:
	pip install --upgrade pip
	pip install -e .

install-dev: install
	pip install --upgrade pip
	pip install -e .[dev]

test: 
	${PYTHON} -m pytest ${TEST_PATH}

vcr-new-episodes:
	${PYTHON} -m pytest ${TEST_PATH} -vvv -s --record-mode=new_episodes
