SHELL := /bin/bash

# Install the package in editable mode or not
install:
ifdef edit
	python -m pip install -e .
else
	python setup.py install
endif


# ie: make config TOKEN=ru=6544564c515s1c5ss32ds15
config:
	@echo "token = '$(TOKEN)'" >> advent_of_code/config__.toml
	@echo "Token saved in advent_of_code/config.toml"


# Delete the python modules' caches
clean:
	find . -type d -name __pycache__ -prune -exec rm -rf {} \;