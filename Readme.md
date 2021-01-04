# SnailSoup Version 1.1 for Mac/Linux

This repository stores the python application that is intended to be used to update an HTML website remotely that is hosted on github pages. It works by first taking HTML page templates and filling them in with HTML objects made with BeautifulSoup4.

### **Instructions**

**Initial Setup**
1. download the latest version of Python at https://www.python.org/downloads/ (Python 3.9)
2. execute the setup.sh file 

**Updating Website**
1. edit the assets folder to represent your view of the website 
2. execute the update.sh file (double check to make sure nothing important is gone, because there's no way to rewind from here)
3. go to xiacindy.github.io to see if it looks how you want it 

### **About the Assets Folder**
1. files are read in alphanumeric order, so to order boxes in a webpage, I recommend naming them with numbers corresponding to their order (ex. 1comic, 2gallery, 3comic, 4project). Images are the same. To order images, rename them so that they correspond to the ordering you like.
2. elements correspond to one of three things: comics, galleries, and projects. Make sure that the end of the folder name corresponds to either **comic**, **gallery**, or **project**, otherwise there might be errors. 
For example: "1comic" creates a comic element in whatever webpage folder... "2comics" or "comic1" does not
3. As of right now, do not mess with the file formatting of assets. Just change what folders are inside each of the webpages (comics, illustrations, index)
4. DON'T TOUCH ICONS! and try not to touch about!

### **Useful Stuff**
1. there is a description.json maker in the gui folder. Double click to open the file or Open terminal and type in `py descriptionmaker.py`
