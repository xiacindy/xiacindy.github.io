### descriptionmaker.py ###
# auxillary application for use with main.py as a GUI for creating new json files without having to edit them in an editor

## prereqs ##
import tkinter as tk
import tkinter.messagebox
import json


## application class ##
class DesMaker:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Description Maker")

        # instructions
        lbl_header = tk.Label(text="Description Maker")
        lbl_instructions = tk.Label(
            text=
            "creates a json file in the folder right outside with all of the following fields filled\n"
        )

        # title entry
        lbl_title = tk.Label(text="Title:")
        self.txt_title = tk.Text(height=10)

        # description entry
        lbl_description = tk.Label(text="Description: (optional)")
        self.txt_description = tk.Text(height=10)

        # link entry
        lbl_link = tk.Label(text="Link: (optional)")
        self.txt_link = tk.Text(height=10)

        # submit button
        btn_submit = tk.Button(self.window,
                               text="Convert",
                               command=self.submit)

        # pack stuff in!!!!
        self.elements = [
            lbl_header, lbl_instructions, lbl_title, self.txt_title,
            lbl_description, self.txt_description, lbl_link, self.txt_link,
            btn_submit
        ]
        [x.pack() for x in self.elements]

    def submit(self):

        # title needs to be present
        if not self.txt_title.get(1.0, tk.END).rstrip("\n"):
            tkinter.messagebox.showwarning("Error", "Title is missing")

        # write to dict and json
        else:
            to_json = dict()
            to_json["title"] = self.txt_title.get(1.0, tk.END).rstrip("\n")
            to_json["description"] = self.txt_description.get(
                1.0, tk.END).rstrip("\n")
            to_json["link"] = self.txt_link.get(1.0, tk.END).rstrip("\n")
            description = json.dumps(to_json, indent=2)
            with open("description.json", "w") as file:
                file.write(description)
            self.window.destroy()

    def run(self):

        self.window.mainloop()


## main ##

if __name__ == "__main__":
    application = DesMaker()
    application.run()