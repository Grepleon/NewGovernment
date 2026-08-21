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

def create_politicians() -> dict[str:path_politician.Politician]:
    _politicians = variable_characters()

    for politician in _politicians:
        data_politician = _politicians[politician]
        data_politician.start()

    return _politicians

politicians = create_politicians()
all_countries, all_areas = variables_country()
nations = variables_nations()

game_state = game_states.GameState(
    dt.datetime(config.first_year[0],
                config.first_year[1],
                config.first_year[2],
                config.first_year[3],
                config.first_year[4]
                ), 0,
    None,
    politicians,
    all_areas,
    all_countries,
    nations,
    None
)


for area_name in all_areas:
    area = all_areas[area_name]
    for city_name in area.cities:
        city = area.cities[city_name]
        sum_p = 0
        min_p = 0
        for pol in politicians:
            polt = politicians[pol]
            print(polt.name, "в городе", city_name, ":", city.vote(polt))
            sum_p += city.vote(polt)
            if city.vote(polt) < min_p:
                min_p = city.vote(polt)
        print(f"ГОРОД {city_name}:")
        for pol in politicians:
            polt = politicians[pol]
            print(f"- {polt.name}: {(-min_p + city.vote(polt)) / sum_p * 100}%")