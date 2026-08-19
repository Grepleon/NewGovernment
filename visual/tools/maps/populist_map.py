from visual.display import Display
from mainloop.game_states import GameState
from hints.colors.lite import lite
import config
from math import log2
from hints.colors.mix import mix

def upload_populist_map(display:Display, game_state:GameState, cities):
    max_val = 20
    max_val2 = 20

    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]

                economic = log2(11 + city.popular_ideas.left_right) / log2(1 + max_val)
                freedom = log2(11 + city.popular_ideas.freedom) / log2(1 + max_val2)

                color = lite(mix("#770000", "#000077", economic), int(freedom * 180))

                cities[name_city].color = color
                display.recolor(color, name_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_area)
                display.recolor(lite(color, -120), name_city + config.pref_text_country)
                display.recolor(color, name_city + config.pref_text_null)