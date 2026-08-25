from visual.display import Display
from mainloop.game_states import GameState
from hints.colors.lite import lite
import config
from math import log2

def upload_popularity_map(display:Display, game_state:GameState, cities):
    max_val = 1000000 / 100000

    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]
                value = log2(1 + max(city.vote(game_state.selected_politician) / 100000, 0)) / log2(1 + max_val)
                if name_country in game_state.selected_politician.citizenship:
                    color = lite("#003300", int(value * 150) + 40)
                else:
                    color = lite("#000033", int(value * 150) + 40)
                cities[name_city].color = color
                display.recolor(color, name_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_area)
                display.recolor(lite(color, -120), name_city + config.pref_text_country)
                display.recolor("YELLOW", name_city + config.pref_text_null)