#!/usr/bin/env bash
BASEDIR=($dirname "$0")

pip3 install -r requirements.txt
cd init || exit
clear
python3 terminal.py