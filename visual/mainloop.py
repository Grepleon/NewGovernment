from tkinter import *
import config

class Display:
    def __init__(self, x, y):
        self.root = Tk()
        self.root.title(config.name_project)
        self.canvas = Canvas(self.root, width=x, height=y, bg=config.bg_color)
        self.canvas.grid()
        self.canvas.pack(anchor=CENTER, expand=1)

    def end(self):
        self.root.mainloop()