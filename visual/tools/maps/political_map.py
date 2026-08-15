from visual.display import Display
from mainloop.game_states import GameState
from hints.lite import lite
import config

def upload_political_map(display: Display, game_state: GameState, cities):
    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]

                cities[name_city].color = country.color
                display.recolor(country.color, name_city)
                display.recolor(lite(country.color, -120), name_city + config.pref_text_city)
                display.recolor(lite(country.color, -120), name_city + config.pref_text_area)
                display.recolor(country.color, name_city + config.pref_text_null)
                display.recolor(country.color, name_city + config.pref_text_country)