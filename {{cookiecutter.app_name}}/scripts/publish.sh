#!/usr/bin/env bash

set -e
set -x

pipenv run python twine upload dist/* ${@}