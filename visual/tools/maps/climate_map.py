from visual.display import Display
from mainloop.game_states import GameState
from hints.colors.lite import lite
from hints.colors.mix import mix
import config
from math import log2


def upload_climate_map(
        display: Display,
        game_state: GameState,
        cities
):
    temperatures = []

    for country in game_state.countries.values():
        for area in country.areas.values():
            for city in area.cities.values():
                temperatures.append(
                    city.geography.average_temperature
                )

    min_val = min(temperatures)
    max_val = max(temperatures)

    value_range = max_val - min_val

    for country in game_state.countries.values():
        for area in country.areas.values():
            for name_city, city in area.cities.items():

                temperature = (
                    city.geography.average_temperature
                )

                if value_range == 0:
                    value = 0.5
                else:
                    shifted_value = temperature - min_val

                    value = (
                        log2(1 + shifted_value)
                        / log2(1 + value_range)
                    )

                # value всегда находится от 0 до 1
                print(city.geography.average_temperature, city.name)
                color = mix(
                    "#00aaff",
                    "#ff00aa",
                    value
                )

                cities[name_city].color = color
                display.recolor(color, name_city)

                text_color = lite(color, -120)

                display.recolor(
                    text_color,
                    name_city + config.pref_text_city
                )
                display.recolor(
                    text_color,
                    name_city + config.pref_text_area
                )
                display.recolor(
                    text_color,
                    name_city + config.pref_text_country
                )
                display.recolor(
                    "YELLOW",
                    name_city + config.pref_text_null
                )