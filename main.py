import config
import politicians.politician as path_politician
import mainloop.game_states as game_states
import visual.display as path_display
from politicians.characters.variables import variable_characters
import visual.managers.all_menu as path_all_menu

def create_politicians() -> dict[str:path_politician.Politician]:
    _politicians = variable_characters()

    for politician in _politicians:
        data_politician = _politicians[politician]
        data_politician.start()

    return _politicians

politicians = create_politicians()

game_state = game_states.GameState(config.first_year, None, politicians)

display = path_display.Display(config.width, config.height)
all_menu = path_all_menu.AllMenu(display, game_state)

all_menu.checker()

display.end()
