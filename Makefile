
.DEFAULT_GOAL := help
ENV := $(CURDIR)/env
PIP := $(ENV)/bin/pip

help:
	@printf "\033[0;33mWelcome the Headsup repo!\n"
	@grep -E '^[0-9a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
	@echo

deps: ## builds dependancies locally
	python -m venv env
	$(PIP) install --upgrade pip setuptools
	$(PIP) install --upgrade -r requirements/base.txt

clean: ## cleans out local env
	rm -rf env/

serve: ## spins up a simple webserver at 8000 with zendesk tables
	. $(ENV)/bin/activate && python -m http.server 8000 --bind 127.0.0.1 &\
	 	. $(ENV)/bin/activate && while true; do python zenquery.py; sleep 30; done

