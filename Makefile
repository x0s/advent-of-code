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


# "make game WHEN=2021/17-2" will launch part 2 of the game issued the 17th, December 2021
game:
	@read AOC_YEAR AOC_DAY AOC_PART <<< $$(echo '$(WHEN)' | perl -pe 's/(20\d{2})\/([01][0-9]|2[0-5])-([12])/$$1 $$2 $$3/');\
	python advent_of_code/year_$$AOC_YEAR/day$$AOC_DAY/part_$$AOC_PART.py


# Launch the tests with verbose or not
test:
ifdef verbose
	python -m unittest discover -v -s tests
else
	python -m unittest discover -s tests
endif


# Delete the python modules' caches
clean:
	@find . -type d -name __pycache__ -prune -exec rm -rf {} \;
	@echo 'Python cache files(compiled bytecode) deleted'