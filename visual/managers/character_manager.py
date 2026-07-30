import visual.managers.manager as manager
import config

class CharacterManager(manager.Manager):
    def __init__(self, display, buttons, id_objects, politicians):
        super().__init__(display, buttons, id_objects)
        self.politicians = politicians

    def test(self):
        for n, i in enumerate(self.buttons):
            print(n, i.name)
        for n, i in enumerate(self.id_objects):
            print(n, i)


    def check(self):
        for _button in self.buttons:
            if _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if self.display.fast_left_button_pressed:
                    for _button2 in self.buttons:
                        if _button2 != _button:  _button2.disable()
                    _button.mouse_clicked_object()
            _button.display_object()

    def active(self):
        self.buttons[-2].hide()
        for i in range(2, 2 + config.quantity_frames):
            if self.buttons[i].on:
                id_object = self.id_objects[3 * (i - 2) + 2]
                self.display.show(id_object)
            else:
                id_object = self.id_objects[3 * (i - 2) + 2]
                self.display.hide(id_object)

            if self.buttons[i].into_mouse:
                self.buttons[-2].show()
                self.buttons[-2].rewrite_text(self.politicians[self.buttons[i].name].to_briefly_str())
                self.buttons[-2].to_move(self.display.mouse_x, self.display.mouse_y)

