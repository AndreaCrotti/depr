#!/usr/bin/env bash

# TODO: get a version number in input to add a git tag

python setup.py register -r pypitest
python setup.py sdist upload -r pypitest
