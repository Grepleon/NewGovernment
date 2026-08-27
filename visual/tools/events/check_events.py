from visual.display import Display
from visual.components.game_event import GameEvent
from mainloop.game_states import GameState

class CheckerEvents:
    def __init__(self, display, game_state, game_event):
        self.display:Display = display
        self.game_state:GameState = game_state
        self.game_event:GameEvent = game_event

    def check(self):
        if self.game_state.get_day() == "00:00 1":
            self.game_event.show()
            self.game_event.rewrite(
                "С новым месяцем!",
                ["Ура!", "", "", "", ""],
            ["Гип-гип, ура!", "", "", "", ""]
            )

