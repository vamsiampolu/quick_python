#!/usr/bin/env bash

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -
echo "PATH=${HOME}/.poetry/bin:${PATH}" >> $GITHUB_ENV
