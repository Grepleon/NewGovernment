from visual.display import Display
from mainloop.game_states import GameState
from politicians.politician import Politician
from random import randint

def carry_out(politician:Politician, display:Display, game_states:GameState):
    pop_factor = politician.get_populist_factors()
    politician.popularity.for_peoples(int(pop_factor / 10 * randint(3, 4)) + 1)
