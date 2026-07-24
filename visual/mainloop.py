from tkinter import *
import config

class Display:
    def __init__(self, x, y):
        self.root = Tk()
        self.root.title(config.name_project)
        self.canvas = Canvas(self.root, width=x, height=y, bg=config.bg_color)
        self.canvas.grid()
        self.canvas.pack(anchor=CENTER, expand=1)
        self.id_objects = 1

    def end(self):
        self.root.mainloop()

    def create_rectangle(self, x1, y1, x2, y2, color, outline, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline, tags=str(self.id_objects))
            return self.id_objects
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline, tags=tag)
        return tag

    def create_circle(self, x1, y1, x2, y2, color, outline, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=outline, tags=str(self.id_objects))
            return self.id_objects
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline, tags=tag)
        return tag

    def create_line(self, x1, y1, x2, y2, color, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_line(x1, y1, x2, y2, fill=color, tags=str(self.id_objects))
            return self.id_objects
        self.canvas.create_line(x1, y1, x2, y2, fill=color, tags=tag)
        return tag

    def create_text(self, x1, y1, text, color, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_text(x1, y1, text=text, fill=color, tags=str(self.id_objects))
            return self.id_objects
        self.canvas.create_text(x1, y1, text=text, fill=color, tags=tag)
        return tag