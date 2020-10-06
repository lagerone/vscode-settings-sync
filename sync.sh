#!/bin/bash -e

BASEDIR=$(dirname "$0")
PREFIX="[vs-sync]"

pushd $BASEDIR

echo "$PREFIX Setting up virtual environment..."
python3 -m venv venv
source "$BASEDIR/venv/bin/activate"

echo "$PREFIX Installing dependencies..."
python -m pip install --upgrade pip
pip install -r ./src/dev_requirements.txt --upgrade

SCRIPT_PATH="$BASEDIR/src/sync_cli.py"
echo "$PREFIX Running script_path $SCRIPT_PATH..."
python $SCRIPT_PATH

echo "$PREFIX Deactivating..."
deactivate

echo "$PREFIX Done."

popd