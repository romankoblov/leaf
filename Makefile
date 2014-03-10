python = python
all: build

build:
	@ $(python) setup.py sdist register upload
