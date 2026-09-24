from visual.display import Display
from mainloop.game_states import GameState
from politicians.politician import Politician
from random import randint, random

def carry_out(politician:Politician, display:Display, game_states:GameState):
    if politician.track >= randint(5, 25): # воровал - тюрьма
        politician.at_large = True
        politician.add_rep(-10)
        return

    politician.add_rep(10)