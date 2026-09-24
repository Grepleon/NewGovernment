from visual.display import Display
from mainloop.game_states import GameState
from politicians.politician import Politician
from random import randint, random

def carry_out(politician:Politician, display:Display, game_states:GameState):
    pop_factor = politician.get_populist_factors()
    politician.popularity.for_elderly(8)