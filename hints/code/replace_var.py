from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its

def replace_var(text:str, game_state:GameState):
    return (text
            .replace("<POP>", its(game_state.selected_politician.popularity.peoples_total()))
            .replace("<SUP>", its(game_state.selected_politician.support.total()))
            .replace("<REP>", its(game_state.selected_politician.reputation))
            .replace("<MONEY>", its(game_state.selected_politician.money))
            .replace("<POLH>", its(game_state.selected_politician.political_hour))
            .replace("</", "<")
        )