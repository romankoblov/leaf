python = python
git = git
nosetests = nosetests

all: clean build

build:
	@ $(python) setup.py clean sdist register upload

clean:
	@ $(git) clean -dfx

test:
	@ $(nosetests) --with-coverage --cover-package=leaf
