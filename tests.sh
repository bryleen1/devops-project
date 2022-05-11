#!/bin/bash
python3 -m venv venv
ls -l
source venv/bin/activate
declare -a directories=("front_end_api" "dare_api" "truth_api" "merge_api")
for dir in "${directories[@]}"
do
    cd ${dir}
    pip3 install -r requirements.txt
    python3 -m pytest --cov=application
    cd ..
done