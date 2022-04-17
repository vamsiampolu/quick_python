#!/usr/bin/env bash

echo "Run tests while typechecking"
poetry run pytest --mypy
