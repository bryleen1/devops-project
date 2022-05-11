#!/bin/bash
python3 -m venv venv
ls -l
source venv/bin/activate
declare -a directories=("service_1" "service_2" "service_3" "service_4")
for dir in "${directories[@]}"
do
    cd ${dir}
    pip3 install -r requirements.txt
    python3 -m pytest --cov=application
    cd ..
done