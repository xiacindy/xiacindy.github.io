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

echo ~~~

if git status | grep "Your branch is ahead of 'origin/main' by" &> 
then
    echo "Pushing data..."
    git push
else
    git status
    echo "No Changes"
fi

sleep 3