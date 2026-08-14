from visual.display import Display
from mainloop.game_states import GameState
from hints.lite import lite

def upload_regional_map(display:Display, game_state:GameState, cities):
    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]

                cities[name_city].color = lite(area.color, -0)
                display.recolor(lite(area.color, -0), name_city)