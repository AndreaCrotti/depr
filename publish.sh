#!/usr/bin/env bash

# TODO: get a version number in input to add a git tag

if [ "$1" == "LIVE" ]
then
    python setup.py register -r pypi
    python setup.py sdist upload -r pypi
else
    python setup.py register -r pypitest
    python setup.py sdist upload -r pypitest
fi
