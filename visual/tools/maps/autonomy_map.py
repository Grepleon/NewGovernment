import config
from visual.display import Display
from mainloop.game_states import GameState
from hints.colors.lite import lite
from math import log2

def upload_autonomy_map(display:Display, game_state:GameState, cities):
    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]

                color = "#005B00"
                val = log2(1 + max(area.autonomy, 0)) / log2(1 + 100)
                color = lite(color, int(val * 200))

                cities[name_city].color = color
                display.recolor(lite(color, -120), name_city)
                display.recolor(lite(color, -120), name_city + config.pref_text_city)
                display.recolor(color, name_city + config.pref_text_null)
                display.recolor(color, name_city + config.pref_text_area)
                display.recolor(color, name_city + config.pref_text_country)
