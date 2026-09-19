from visual.display import Display
from mainloop.game_states import GameState
from politicians.politician import Politician
from random import randint, random

def carry_out(politician:Politician, display:Display, game_states:GameState):
    pop_factor = politician.get_populist_factors()
    if pop_factor > random() * 20: #интервью прошло удачно
        politician.popularity.add_all(randint(4, 6))
    else: # неудачное интервью
        politician.popularity.add_all(-randint(3, 5))
        politician.add_rep(-randint(1, 2))
