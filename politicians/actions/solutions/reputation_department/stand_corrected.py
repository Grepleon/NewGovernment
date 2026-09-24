from visual.display import Display
from mainloop.game_states import GameState
from politicians.politician import Politician
from random import randint, random

def carry_out(politician:Politician, display:Display, game_states:GameState):
    politician.add_rep(randint(2, 4))