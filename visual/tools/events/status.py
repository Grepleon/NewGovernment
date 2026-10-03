from visual.display import Display
from visual.components.game_event import GameEvent
from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its
import random

def death(self, game_state: GameState):
    return not game_state.selected_politician.alive