from Webpage import *

index = Webpage("index")
illustrations = Webpage("illustrations")
comic = Webpage("comics")

Webpage_list = [index, illustrations, comic]
for page in Webpage_list:
    page.update()

print("\n UPDATING WEBSITE... \n")