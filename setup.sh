#!/bin/bash

# Setup.sh - Bash Script to setup environment 

# checks for beautifulsoup4
if pip list | grep beautifulsoup4 &> /dev/null
then
    echo bs4 already installed...
else
    echo installing bs4...
    echo ~~~~~~
    pip install beautifulsoup4
    echo ~~~~~~
fi

# clones the repository 

if ls -a | grep cindyxia20.github.io &> /dev/null
then
    echo git repo is already cloned...
else 
    echo cloning git repo...
    echo ~~~~~~
    git clone https://github.com/cindyxia20/cindyxia20.github.io.git
    echo ~~~~~~
fi 

echo setup complete!
sleep 3

