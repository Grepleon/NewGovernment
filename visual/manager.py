import visual.components.button as button

class Manager:
    def __init__(self, display, buttons, id_objects):
        self.display = display
        self.buttons:list[button.Button] = buttons
        self.id_objects:list[str|int] = id_objects

    def check(self):
        for _button in self.buttons:
            if _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if self.display.left_button_pressed:
                    _button.mouse_clicked_object()
            _button.display_object()

    def delete(self):
        for _button in self.buttons:
            _button.delete()

        for id_object in self.id_objects:
            self.display.delete(id_object)

    def hide(self):
        for _button in self.buttons:
            _button.hide()

        for id_object in self.id_objects:
            self.display.hide(id_object)

    def show(self):
        for _button in self.buttons:
            _button.show()

        for id_object in self.id_objects:
            self.display.show(id_object)


