# SnailSoup Version 1.0

This repository stores the python application that is intended to be used to update an HTML website remotely that is hosted on github pages. It works by first taking HTML page templates and filling them in with HTML objects made with BeautifulSoup4.

in progress....

### **Instructions**

**Initial Setup**
1. download the latest version of Python at https://www.python.org/downloads/ (Python 3.9)
2. download the latest version of Gitbash for Windows at https://git-scm.com/download/win (Git for Windows 2.29.2 64bit)
3. execute the setup.sh file 

**Updating Website**
1. edit the assets folder to represent your view of the website 
2. execute the update.sh file 
3. go to cindyxia20.github.io to see if it looks how you want it 

### **About the Assets Folder**
1. will do later__

### **Useful Stuff**
1. there is a description.json maker in the gui folder. Open terminal and type in `py descriptionmaker.py`

DEVELOPER STUFF ~~~

Things to add:
1. MAKE AN INSTALLER? setup_tools? conda environment?
2. make the application more modular
    a. make a website class with dynamic webpages (# of folders is changeable)
    b. make a gui to make it easier to update everything !!
3. add more elements

Prerequisities: Setup Script
1. install beautifulsoup4
2. git clone https

Procedure: Shell Script 
1. git pulls if changes have been made - gets latest python scripts
2. runs main python file 
3. git add . 
4. git commit -m "auto commit"
5. git push

