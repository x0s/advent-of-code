SHELL := /bin/bash

all: help

.PHONY: help
help:
	@echo "Available targets:"
	@echo "   install [EDIT=1]              : Install the package (pass EDIT for editable mode)"
	@echo "   config TOKEN=<TOKEN>          : Generate the config file"
	@echo "   game WHEN=<YEAR>/<DAY>-<PART> : Launch a solution (ie: make game WHEN=2022/01-2)"
	@echo "   test [VERBOSE=1]              : Launch the tests locally (pass VERBOSE to enumerate the tests)"
	@echo "   test_this DAY=<YEAR>/<DAY>    : Launch the tests case covering only one day (ie: make test_this DAY=2022/02)"
	@echo "   coverage                      : Generate & display test coverage report"
	@echo "   clean                         : Delete python bytecode cache"


##########################################################################
# Setting up
##########################################################################

# Install the package in editable mode or not
.PHONY: install
install:
ifdef EDIT
	python -m pip install -e .
else
	python -m pip install .
endif

# ie: make config TOKEN=ru=6544564c515s1c5ss32ds15
.PHONY: config
config:
	@echo "token = '$(TOKEN)'" > advent_of_code/config.toml
	@echo "Token saved in advent_of_code/config.toml"

.PHONY: build
build:
	@docker build --tag aoc-image -f Dockerfile .
# make "make_in_container" command available when conda env is activated
ifdef CONDA_PREFIX
	@$(eval PATH_ALIAS := ${CONDA_PREFIX}/etc/conda/activate.d/aliases_.sh)
	@mkdir -p ${CONDA_PREFIX}/etc/conda/activate.d
	@echo "#!/bin/bash" >> $(PATH_ALIAS)
	@echo "alias make_in_container='make -f Makefile_docker'" >> $(PATH_ALIAS)
	@source $(PATH_ALIAS)
endif


##########################################################################
# Running the app
##########################################################################

.PHONY: run
run:
	@docker run -it --detach aoc-image bash


# "make game WHEN=2021/17-2" will launch part 2 of the game issued the 17th, December 2021
.PHONY: game
.ONESHELL:
game:
	@read AOC_YEAR AOC_DAY AOC_PART <<< $$(echo '$(WHEN)' | perl -pe 's/(20\d{2})\/([01][0-9]|2[0-5])-([12])/$$1 $$2 $$3/')
	python advent_of_code/year_$$AOC_YEAR/day_$$AOC_DAY/part_$$AOC_PART.py


##########################################################################
# Testing / Cleaning
##########################################################################

# Launch the tests with verbose or not
.PHONY: test
test:
ifdef VERBOSE
	python -m unittest discover -v -s tests
else
	python -m unittest discover -s tests
endif


# Launch tests case for only one day (we suppose we want details/verbose here)
# Example: "make test_this DAY=2022/02" will launch test covering day 2 of 2022
.PHONY: test_this
.ONESHELL:
test_this:
	@read AOC_YEAR AOC_DAY <<< $$(echo '$(DAY)' | perl -pe 's/(20\d{2})\/([01][0-9]|2[0-5])/$$1 $$2/')
	python -m unittest -v tests/$$AOC_YEAR/test_day_$$AOC_DAY.py

.PHONY: coverage
coverage:
	@coverage run -m unittest
	@coverage report

# Delete the python modules' caches
.PHONY: clean
clean:
	@find . -type d -name __pycache__ -prune -exec rm -rf {} \;
	@echo 'Python cache files(compiled bytecode) deleted'