import visual.components.button as button

class Manager:
    def __init__(self, display, buttons):
        self.display = display
        self.buttons:list[button.Button] = buttons

    def check(self):
        for _button in self.buttons:
            _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y)
            _button.display_object()