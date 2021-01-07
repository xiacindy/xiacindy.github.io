from Webpage import *

if __name__ == "__main__":
    
    try:
        index = Webpage("index")
        illustrations = Webpage("illustrations")
        comic = Webpage("comics")

        Webpage_list = [index, illustrations, comic]
        for page in Webpage_list:
            page.update()

        print("\n DONE UPDATING WEBSITE... NO ERRORS\n")
    
    except:
        print("Error 420: FATAL ERROR MAKING DESCRIPTION")