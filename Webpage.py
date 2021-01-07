import os
import json
import html
from bs4 import BeautifulSoup

#### Banned List ####


glo_bannedlist = [
    ".DS_Store"
]

#### HTMLELEMENT Object ####


class HtmlElement:  # parent class
    def __init__(self, webpage, dir_name, html_page):
        self.soup = BeautifulSoup(open(html_page + ".html", encoding='utf-8'),
                                  "html.parser")
        self.dir_name = dir_name
        self.html_page = html_page
        path = "assets/" + webpage + "/" + dir_name
        self.files = sorted([(path + "/" + f) for f in os.listdir(path) if f.rsplit("/") not in glo_bannedlist])

    # string
    def __str__(self):
        return self.soup.prettify()

    # writes to html file
    def update(self):
        result = self.soup.prettify("utf-8")
        with open(self.html_page + ".html", "wb") as file:
            file.write(result)


#### Project Object ####


class Project(HtmlElement):  # contains description
    def __init__(self, webpage, dir_name, html_page):
        # inherit needed elements
        HtmlElement.__init__(self, webpage, dir_name, html_page)

        # gets and parses through description -->
        try:
            describe = [x for x in self.files if x.endswith(".json")][0]
            with open(describe, "r", encoding='utf-8') as txt:
                description = json.load(txt)
                self.title = description["title"]
                self.description = description["description"]
                self.link = description["link"]
        except:
            print("\nError 69: NO DESCRIPTION/BROKEN DESCRIPTION.JSON. PLEASE BUILD NEW DESCRIPTION.JSON FILE\n")
            self.title = "NO TITLE"
            self.description = "NO DESCRIPTION"
            self.link = ""
        
        self.img_paths = [x for x in self.files if not (x.endswith(".json"))]

    def make_project(self):
        projects = self.soup.find("section", id="projects")
        div = self.soup.new_tag("div", **{'class': 'project'})

        # description and title and link
        title = self.soup.new_tag("h1")
        title.string = self.title
        if self.link:
            link = self.soup.new_tag("a",
                                     href=self.link,
                                     target="_blank",
                                     rel="noopener noreferrer")
            link.append(title)
            title = link
        description = self.soup.new_tag("p")
        description.string = self.description

        # img grid
        img_grid = self.soup.new_tag("div", **{'class': 'project-grid'})
        for path in self.img_paths:
            img = self.soup.new_tag("img", src=path)
            img_grid.append(img)

        # append everything togther
        div.append(title)
        div.append(description)
        div.append(img_grid)
        projects.append(div)


### Gallery Object ###


class Gallery(HtmlElement):
    def make_gallery(self):
        galleries = self.soup.find("section", id="galleries")
        gallery = self.soup.new_tag("div", **{'class': 'gallery'})
        for img_path in self.files:
            tag = self.soup.new_tag("img", src=img_path)
            gallery.append(tag)
        galleries.append(gallery)


### Comic Element ###


class Comic(Project):
    def make_comic(self):
        comics = self.soup.find("section", id="comics")
        comic_object = self.soup.new_tag("div", **{'class': 'comic-object'})

        # create A with title and description
        item_a = self.soup.new_tag("span", **{'class': 'grid-item item-a'})
        title = self.soup.new_tag("h1")
        title.string = self.title
        if self.link:
            link = self.soup.new_tag("a",
                                     href=self.link,
                                     target="_blank",
                                     rel="noopener noreferrer")
            link.append(title)
            title = link
        description = self.soup.new_tag("p")
        description.string = self.description

        item_a.append(title)
        item_a.append(description)

        # create B with comic object and buttons
        item_b = self.soup.new_tag("span", **{'class': 'grid-item item-b'})
        comic = self.soup.new_tag("div", **{'class': 'comic'})
        comic['data-slide-index'] = '0'

        for path in self.img_paths:
            img = self.soup.new_tag("img", src=path, **{'class': 'comic-page'})
            comic.append(img)
        button_left = self.soup.new_tag(
            "button",
            **{"class": "comic-left comic-button"},
            onclick="prevComic(this.parentElement, '.comic')")
        button_left.string = html.unescape("&#10094")
        button_right = self.soup.new_tag(
            "button",
            **{"class": "comic-right comic-button"},
            onclick="nextComic(this.parentElement, '.comic')")
        button_right.string = html.unescape("&#10095")
        item_b.append(comic)
        item_b.append(button_left)
        item_b.append(button_right)

        # append everything together
        comic_object.append(item_a)
        comic_object.append(item_b)
        comics.append(comic_object)


### WebPage Object ###


class Webpage:
    def __init__(self, dir_name, html_page=None):
        if html_page is None:
            html_page = dir_name
        self.html_page = html_page
        self.soup = BeautifulSoup(open(html_page + ".html", encoding='utf-8'),
                                  "html.parser")
        path = "assets/" + dir_name
        self.files = sorted([(path + "/" + f) for f in os.listdir(path) if f.rsplit("/") not in glo_bannedlist])

    def update(self):
        self._clear()
        names = [path.rsplit("/")[-1] for path in self.files]
        for object_dir in names:
            if object_dir.endswith("project"):
                project = Project(self.html_page, object_dir, self.html_page)
                project.make_project()
                project.update()
            if object_dir.endswith("gallery"):
                gallery = Gallery(self.html_page, object_dir, self.html_page)
                gallery.make_gallery()
                gallery.update()
            if object_dir.endswith("comic"):
                comic = Comic(self.html_page, object_dir, self.html_page)
                comic.make_comic()
                comic.update()

    def _clear(self):
        sections = self.soup.find_all("section")
        for tag in sections:
            tag.clear()
        result = self.soup.prettify("utf-8")
        with open(self.html_page + ".html", "wb") as file:
            file.write(result)
