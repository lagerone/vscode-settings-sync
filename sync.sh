#!/bin/bash

BASEDIR=$(dirname "$0")

pushd $BASEDIR

source venv/bin/activate
python src/sync_cli.py
deactivate

popd