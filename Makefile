python = python
git = git

all: clean build

build:
	@ $(python) setup.py clean sdist register upload

clean:
	@ $(git) clean -dfx
