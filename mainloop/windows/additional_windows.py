from visual.components.base_object import BaseObject as GameObject

from visual.display import Display
from visual.components.base_object import BaseObject

class AdditionalWindow:
    def __init__(self, name_window, game_state, display):
        self.name_window:str = name_window
        self.game_state:"GameState" = game_state
        self.display:Display = display
        self.objects:list[str] = []
        self.components:list[GameObject] = []

    def created(self):
        pass

    def check_activity(self):
        try:
            self.display.activity_windows[self.name_window] = \
                self.display.roots[self.name_window].winfo_exists()
        except Exception:
            self.display.activity_windows[self.name_window] = 0
        return self.display.activity_windows[self.name_window]

    def base_process(self):
        if self.check_activity():
            self.display.switch_window(self.name_window)
            for button in self.components:
                if button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                    if self.display.fast_left_button_pressed:
                        button.mouse_clicked_object()
                button.display_object()
            self.display.switch_window(self.display.main_window)


    def process(self):
        pass

