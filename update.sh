#!/bin/bash

# update.sh
# updates the html files and pushes them to github

cd "/Users/cindyxia/Desktop/GitHub Portfolio/xiacindy.github.io"

# first git pulls any changes off of github (for updates to python scripts)

git pull

# runs main.py

python3 main.py

sleep 1

# git push

git add .
git commit -m "auto commit"

echo ~~~

git push -u origin main

sleep 3
