from visual.display import Display
from mainloop.game_states import GameState
from hints.lite import lite
import config
from math import log2

def upload_gdp_per_capita_map(display:Display, game_state:GameState, cities):
    max_val = 0
    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]
                max_val = max(max_val, city.budget // city.peoples)

    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]
                value = log2(1 + max(city.budget // city.peoples, 0)) / log2(1 + max_val)
                color = lite("#000011", int(value * 200))
                cities[name_city].color = color
                display.recolor(color, name_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_area)
                display.recolor(lite(color, -120), name_city + config.pref_text_country)
                display.recolor("WHITE", name_city + config.pref_text_null)