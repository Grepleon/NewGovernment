from visual.display import Display
from mainloop.game_states import GameState
from hints.colors.lite import lite
import config
from math import log2
from config import electricity
def upload_specific_resources_map(display:Display, game_state:GameState, cities, res:str):
    max_val = 0
    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]
                max_val = max(max_val, 0 if not res in city.resources else city.resources[res].explored_quantity)
                if res == electricity:
                    max_val = max(max_val, 0 if not res in city.resources else city.resources[res].extracted)

    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]
                value = (log2(1 + max(0 if not res in city.resources else city.resources[res].explored_quantity, 0
                                     if res != electricity else city.resources[res].extracted))
                         / (log2(1 + max_val) + 0.001))
                color = lite("#000055", int(value * 200) - 50)
                cities[name_city].color = color
                display.recolor(color, name_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_area)
                display.recolor(lite(color, -120), name_city + config.pref_text_country)
                display.recolor(lite(color, -120), name_city + config.pref_text_null)