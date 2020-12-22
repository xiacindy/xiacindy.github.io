# SnailSoup

This repository stores the python application that is intended to be used to update an HTML website remotely that is hosted on github pages. It works by first taking HTML page templates and filling them in with HTML objects made with BeautifulSoup4.

in progress....

Issues:
1. github push login credentials are weird...

Things to add:
1. MAKE AN INSTALLER 
    s. install dependencies!
    a. git clone repo 
    b. git pull 
    c. create a readme.txt outside cloned repo
2. make the application more modular
    a. make a website class with dynamic webpages (# of folders is changeable)
    b. make a gui to make it easier to update everything 
3. add more elements
4. make a description json maker !!


Prerequisities: Setup Script
1. Python 3.8
2. BeautifulSoup4
3. Gitbash

Procedure: Shell Script 
1. git pulls if changes have been made - gets latest python scripts
2. runs main python file 
3. git add . 
4. git commit -m "auto commit"
5. git push

Version 1.0