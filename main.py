import config
import politicians.politician as path_politician
import mainloop.game_states as game_states
import visual.display as path_display
from loader.load_data import variable_characters, variables_nations
from loader.load_data import variables_country, variable_parties
import visual.menu_builder.all_menu as path_all_menu
import statistics as st
import datetime as dt
from hints.code.execute import execute

statistics:st.Statistics = st.get_statistics()

def create_politicians() -> dict[str:path_politician.Politician]:
    _politicians = variable_characters()

    for politician in _politicians:
        data_politician = _politicians[politician]
        data_politician.start()

    return _politicians

politicians = create_politicians()
all_countries, all_areas = variables_country()
nations = variables_nations()
parties = variable_parties()

display = path_display.Display(config.width, config.height)

game_state = game_states.GameState(
    dt.datetime(config.first_year[0],
                config.first_year[1],
                config.first_year[2],
                config.first_year[3],
                config.first_year[4]
                ), 0,
    politicians["NULL"],
    politicians,
    all_areas,
    all_countries,
    nations,
    statistics,
    parties,
    display
)

all_menu = path_all_menu.AllMenu(display, game_state)

all_menu.checker()

display.end()

st.save(statistics, game_state)
st.set_statistics(statistics)