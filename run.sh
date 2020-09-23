#!/bin/bash -e

CWD=`dirname "$0"`
PREFIX="[vs-sync]"
SCRIPT_PATH="$CWD/src/video_editor_cli.py"
source "$CWD/venv/bin/activate"
echo "$PREFIX Installing dependencies..."
python -m pip install --upgrade pip
pip install -r ./src/dev_requirements.txt --upgrade
pip install -r ./src/requirements.txt --upgrade
echo "$PREFIX Running script_path $SCRIPT_PATH..."
python $SCRIPT_PATH
echo "$PREFIX Deactivating..."
deactivate
echo "$PREFIX Done."