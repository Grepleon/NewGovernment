import visual.components.button as button
import config
from mainloop.game_states import GameState
from visual.components.base_object import BaseObject
from visual.display import Display

class GameEvent(BaseObject):
    def __init__(self, x1, y1, x2, y2, out, quantity_buttons, size_button,
                 texts,
                 color, bg_color, active_color, bg_active_color,
                 text, tag, display: Display, name="NULL"):
        super().__init__(tag, display)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.color, self.bg_color, self.active_color, self.bg_active_color = \
            color, bg_color, active_color, bg_active_color
        self.text = text
        self.pref_text = "-T"
        self.name = name

        self.out = out
        self.quantity_buttons = quantity_buttons
        self.size_button = size_button
        self.texts = texts

        self.into_mouse = False
        self.on = False

        self.buttons = []
        self._create()

    def _create(self):
        self.display.create_rectangle(self.x1, self.y1, self.x2, self.y2, self.bg_color, self.color, self.object_id)
        for index in range(self.quantity_buttons):
            self.buttons.append(
                button.Button(
                    self.x1 + self.out,
                    self.y2 + (- self.out - self.size_button) * (index + 1) - self.out - self.out * index,
                    self.x2 - self.out,
                    self.y2 + (- self.out - self.size_button) * index - self.out - self.out * index,
                    self.color,
                    self.bg_color,
                    self.active_color,
                    self.bg_active_color,
                    self.texts[index],
                    self.display.add_id(),
                    self.display

                )
            )

        self.display.create_text(self.x1 / 2 + self.x2 / 2,
            (self.y2 + (- self.out - self.size_button) * self.quantity_buttons
                                 - self.out - self.out * self.quantity_buttons + self.y1) / 2,
                                 self.text, self.color)

