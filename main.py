from time import time
import config
import politicians.politician as path_politician
import mainloop.game_states as game_states
import visual.display as path_display
from politicians.characters.variables import variable_characters, variables_nations
from politicians.characters.variables import variables_country
import visual.menu_builder.all_menu as path_all_menu
import statistics as st
import datetime as dt

statistics:st.Statistics = st.get_statistics()

def create_politicians() -> dict[str:path_politician.Politician]:
    _politicians = variable_characters()

    for politician in _politicians:
        data_politician = _politicians[politician]
        data_politician.start()

    return _politicians

politicians = create_politicians()
all_countries = variables_country()
nations = variables_nations()

game_state = game_states.GameState(
    dt.datetime(config.first_year[0], config.first_year[1], config.first_year[2], config.first_year[3], config.first_year[4]),
    None,
    politicians,
    all_countries,
    nations,
    statistics
)

display = path_display.Display(config.width, config.height)
all_menu = path_all_menu.AllMenu(display, game_state)

all_menu.checker()

display.end()

statistics.time += time() - statistics.time_start
st.set_statistics(statistics)