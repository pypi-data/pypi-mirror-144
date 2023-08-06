.PHONY: install
install:
	pip install --upgrade pip setuptools wheel
	pip install -r requirements.txt

.PHONY: install-dev
install-dev: install
	pip install -r requirements-dev.txt
	python3 setup.py develop

.PHONY: build
build:
	python3 setup.py build

.PHONY: lint
lint:
	flake8 chaosdynatrace/ tests/
	isort --check-only --profile black chaosdynatrace/ tests/
	black --check --diff --line-length=80 chaosdynatrace/ tests/

.PHONY: format
format:
	isort --profile black chaosdynatrace/ tests/
	black --line-length=80 chaosdynatrace/ tests/

.PHONY: tests
tests:
	pytest
