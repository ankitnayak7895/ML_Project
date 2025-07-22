#!/bin/bash

echo "[$(date)]:START"

echo "[$(date)]:creating env with python 3.8-version"
conda create --prefix ./env python=3.8 -y

echo "[$(date)]:activating the environment"
source ~/Downloads/anaconda3/etc/profile.d/conda.sh
conda activate "$(pwd)/env"

echo "[$(date)]:installing the dev requirements"
pip install -r requirements.txt

echo "[$(date)]:END"
