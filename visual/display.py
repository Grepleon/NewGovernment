from tkinter import *
import config

class Display:
    def __init__(self, x, y):
        self.root = Tk()
        self.root.title(config.name_project)
        self.canvas = Canvas(self.root, width=x, height=y, bg=config.bg_color)
        self.canvas.pack(anchor=CENTER, expand=1)
        self.id_objects = 1

        self.pref_tag = "Object:"
        self.images = []

        self.left_button_pressed = False
        self.fast_left_button_pressed = False
        self.right_button_pressed = False
        self.mouse_x = 0
        self.mouse_y = 0
        self.mouse_x_root = 0
        self.mouse_y_root = 0
        self.pressed_keys = set()  # Множество для хранения всех нажатых клавиш

        self.info_root: list[Tk] = []

        self.root.bind('<Button-1>', self.on_press)
        self.root.bind('<ButtonRelease-1>', self.on_release)
        self.root.bind('<Button-3>', self.right_on_press)
        self.root.bind('<ButtonRelease-3>', self.right_on_release)
        self.root.bind('<Motion>', self.on_motion)
        self.root.bind('<KeyPress>', self.on_key_press)
        self.root.bind('<KeyRelease>', self.on_key_release)

        self.tact = 0

    def right_on_press(self, event):
        if event.num == 3:
            self.right_button_pressed = True

    def right_on_release(self, event):
        pass

    def on_motion(self, event):
        self.mouse_x = event.x
        self.mouse_y = event.y
        self.mouse_x_root = event.x_root
        self.mouse_y_root = event.y_root

    def on_press(self, event):
        if event.num == 1:
            self.left_button_pressed = True
            self.mouse_x = event.x
            self.mouse_y = event.y
            self.mouse_x_root = event.x_root
            self.mouse_y_root = event.y_root

    def on_release(self, event):
        if event.num == 1:
            self.left_button_pressed = False
            self.fast_left_button_pressed = True
            self.mouse_x = event.x
            self.mouse_y = event.y
            self.mouse_x_root = event.x_root
            self.mouse_y_root = event.y_root

    def on_key_press(self, event):
        self.pressed_keys.add(event.keysym)  # Добавляем клавишу в множество

    def on_key_release(self, event):
        self.pressed_keys.discard(event.keysym)  # Удаляем клавишу из множества

    def end(self):
        self.root.mainloop()

    def create_rectangle(self, x1, y1, x2, y2, color, outline, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline,
                                         tags=self.pref_tag + str(self.id_objects))
            return self.pref_tag + str(self.id_objects)
        self.canvas.create_rectangle(x1, y1, x2, y2, fill=color, outline=outline, tags=str(tag))
        return str(tag)

    def create_circle(self, x1, y1, x2, y2, color, outline, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=outline,
                                    tags=self.pref_tag + str(self.id_objects))
            return self.pref_tag + str(self.id_objects)
        self.canvas.create_oval(x1, y1, x2, y2, fill=color, outline=outline, tags=str(tag))
        return str(tag)

    def create_line(self, x1, y1, x2, y2, color, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_line(x1, y1, x2, y2, fill=color,
                                    tags=self.pref_tag + str(self.id_objects))
            return self.pref_tag + str(self.id_objects)
        self.canvas.create_line(x1, y1, x2, y2, fill=color, tags=str(tag))
        return str(tag)

    def create_text(self, x1, y1, text, color, tag=None) -> int | str:
        if tag is None:
            self.id_objects += 1
            self.canvas.create_text(x1, y1, text=text, fill=color,
                                    tags=self.pref_tag + str(self.id_objects))
            return self.pref_tag + str(self.id_objects)
        self.canvas.create_text(x1, y1, text=text, fill=color, tags=str(tag))
        return str(tag)

    def create_image(self, x1, y1, path, tag=None) -> int | str:
        image = PhotoImage(file=path)
        self.images.append(image)

        if tag is None:
            self.id_objects += 1
            self.canvas.create_image(x1, y1, anchor=NW, image=image,
                                     tags=self.pref_tag + str(self.id_objects))
            return self.pref_tag + str(self.id_objects)
        self.canvas.create_image(x1, y1, anchor=NW, image=image,
                                 tags=self.pref_tag + str(tag))
        return str(tag)

    def create_polygon(self, points, color, outline="black", stipple="", tag=None):
        coordinates = [coordinate for point in points for coordinate in points]
        id_object = str(tag)
        if tag is None:
            self.id_objects += 1
            id_object = self.pref_tag + str(self.id_objects)
        self.canvas.create_polygon(*coordinates, fill=color, outline=outline, stipple=stipple, tags=id_object)

        return id_object

    def add_id(self) -> str:
        self.id_objects += 1
        return self.pref_tag + str(self.id_objects)

    def delete(self, tag):
        self.canvas.delete(str(tag))

    def recolor(self, color, tag):
        self.canvas.itemconfig(str(tag), fill=color)

    def recolor_outline(self, color, tag):
        self.canvas.itemconfig(str(tag), outline=color)

    def rewrite_text(self, text, tag):
        self.canvas.itemconfig(str(tag), text=text)

    def update_fun(self, fun, sec):
        self.canvas.after(sec, fun)

    def show(self, tag):
        self.canvas.itemconfig(tag, state='normal')

    def hide(self, tag):
        self.canvas.itemconfig(tag, state='hidden')

    def move_to_coord(self, tag, new_x1, new_y1, new_x2, new_y2):
        self.canvas.coords(tag, new_x1, new_y1, new_x2, new_y2)

    def move_to_coord2(self, tag, new_x1, new_y1):
        self.canvas.coords(tag, new_x1, new_y1)

    def move(self, tag, dx, dy):
        self.canvas.move(tag, dx, dy)
