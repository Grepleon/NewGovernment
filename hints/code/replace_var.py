from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its

def full_var(text:str, game_state:GameState):
    return (text
            .replace("<FULL-POP>", game_state.selected_politician.popularity.to_str_without_statuses())
            .replace("<FULL-SUP>", game_state.selected_politician.support.to_str_without_statuses())
        )

def base_var(text:str, game_state:GameState):
    return (text
            .replace("<POP>", its(game_state.selected_politician.popularity.peoples_total()))
            .replace("<SUP>", its(game_state.selected_politician.support.total()))
            .replace("<REP>", its(game_state.selected_politician.reputation))
            .replace("<MONEY>", its(game_state.selected_politician.money))
            .replace("<POLH>", its(game_state.selected_politician.political_hour))
            .replace("<CITY>", game_state.selected_politician.location)
            .replace("</", "<")
        )

def replace_var(text:str, game_state:GameState):
    text = base_var(text, game_state)
    text = full_var(text, game_state)
    return text