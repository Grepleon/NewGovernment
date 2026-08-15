from visual.display import Display
from mainloop.game_states import GameState
from hints.lite import lite
import config
from math import log2

def upload_ethnic_map(display:Display, game_state:GameState, cities):
    max_val = 100

    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]
                most_nation = max(city.nations, key= lambda x: x.count)
                value = log2(1 + max(int(most_nation.count * 100), 0)) / log2(1 + max_val) - 0.85
                color = lite(game_state.nations[most_nation.nation].color, int(2 * value * 250))
                cities[name_city].color = color
                display.recolor(color, name_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_area)
                display.recolor(lite(color, -120), name_city + config.pref_text_country)
                display.recolor(color, name_city + config.pref_text_null)