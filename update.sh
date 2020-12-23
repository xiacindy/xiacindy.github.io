#!/bin/bash

# update.sh 
# updates the html files and pushes them to github

# first git pulls any changes off of github (for updates to python scripts)

git pull 

# runs main.py 

py main.py

sleep 1

# git push 

git add .
git commit -m "auto commit"
if [ -n "$(git status - porcelain)" ];
then
    echo "No Changes"
else
    git status
    echo "Pushing data..."
    git push
fi

sleep 5