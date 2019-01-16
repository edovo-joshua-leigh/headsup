
.DEFAULT_GOAL := help
ENV := $(CURDIR)/env
PIP := $(ENV)/bin/pip
HEADPY := $(ENV)/bin/python

help:
	@printf "\033[0;33mWelcome the Headsup repo!\n"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

deps: ## builds dependancies locally
	python3 -m venv env
	$(PIP) install --upgrade pip setuptools
	$(PIP) install --upgrade -r requirements/base.txt

clean: ## cleans out local env
	rm -rf env/

test_dashboard: ## assumes token in file token, served at localhost:8000
	TOKEN=$(shell cat token) INDEX_PATH=$(CURDIR) \
	$(HEADPY) zenquery.py
	$(HEADPY) -m http.server 8000 --bind 127.0.0.1

