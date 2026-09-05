from visual.components.button import Button
import config
from mainloop.game_states import GameState
from visual.components.base_object import BaseObject
from visual.display import Display

class ButtonsGroup(BaseObject):
    def __init__(self, buttons, tag ,display, name="NULL"):
        super().__init__(tag, display)
        self.name = name
        self.buttons:list[Button] = buttons
        self.selected_button = None

    def display_object(self):
        if self.selected_button is None:
            return

    def mouse_into_object(self, x1, y1):
        return True

    def mouse_clicked_object(self):
        selected_button = self.selected_button
        for button in self.buttons:
            if button.on and self.selected_button != button:
                if not self.selected_button is None:
                    self.selected_button.on = False
                self.selected_button = button