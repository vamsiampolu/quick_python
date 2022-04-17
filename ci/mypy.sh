#!/usr/bin/env bash

echo "Just check the types in src files"
poetry run mypy --package quick_python --namespace-packages
