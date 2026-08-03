import visual.components.base_object as base_object

class Manager:
    def __init__(self, display, buttons, id_objects):
        self.display = display
        self.buttons:list[base_object.BaseObject] = buttons
        self.id_objects:list[str|int] = id_objects

    def check(self):
        for _button in self.buttons:
            if _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if self.display.fast_left_button_pressed:
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

    def active(self):
        pass
