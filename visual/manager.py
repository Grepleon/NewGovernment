import visual.components.button as button

class Manager:
    def __init__(self, display, buttons):
        self.display = display
        self.buttons:list[button.Button] = buttons

    def check(self):
        for _button in self.buttons:
            if _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if self.display.left_button_pressed:
                    _button.mouse_clicked_object()
            _button.display_object()

    def delete(self):
        pass