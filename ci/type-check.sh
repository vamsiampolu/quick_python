#!/usr/bin/env bash

echo "Type checking the tests"
poetry run pytest --mypy -m mypy 
