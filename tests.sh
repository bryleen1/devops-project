#!/bin/bash
declare -a directories=("front_end_api" "dare_api" "truth_api" "merge_api")
for dir in "${directories[@]}"
do
  cd ${dir}
  sudo apt-get update
  sudo apt-get install python3 python3-pip python3-venv
  python3 -m venv venv
  source venv/bin/activate
  pip3 install -r requirements.txt
  python3 -m pytest --cov=application
  deactivate
  cd ..
done