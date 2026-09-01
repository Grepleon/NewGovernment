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
        for button in self.buttons:
            if button.object_id == self.selected_button:
                button.on = True
            else:
                button.on = False

    def mouse_into_object(self):
        return True

    def mouse_clicked_object(self):
        selected_button = self.selected_button
        for button in self.buttons:
            if button.on:
                self.selected_button = button.object_id

        for button in self.buttons:
            if button.object_id == selected_button:
                button.on = False