import visual.menu_builder.managers.play_manager as manager
import visual.components.noice as path_noice
import mainloop.game_states as game_states
import visual.components.hint as hint
import config
import visual.components.city as comp_city
from visual.components.area import *
from visual.components.button import Button

def get_menu(display, game_state:game_states.GameState):
    buttons = []

    id_objects_in_main_menu = []

    areas = create_area_backgrounds(display, game_state.countries,
                        (0, 0, config.width, config.height),
                                    max_distance=config.area_radius,
                                    background_color=config.bg_color)
    id_objects_in_main_menu += areas

    cities = []
    dict_cities = {}
    for name_country in game_state.countries:
        country = game_state.countries[name_country]
        for name_area in country.areas:
            area = country.areas[name_area]
            for name_city in area.cities:
                city = area.cities[name_city]
                c_city = comp_city.VisualObjectCity(
                                      city.location.x - city.peoples ** 0.5 / 2,
                                      city.location.y - city.peoples ** 0.5 / 2,
                                      city.location.x + city.peoples ** 0.5 / 2, # / config.size_cty,
                                      city.location.y + city.peoples ** 0.5 / 2, # / config.size_cty,
                                      city, area, country, display.add_id(), display)
                cities.append(c_city)
                dict_cities[name_city] = c_city

    buttons += cities

    buttons.append(Button(config.coord_year_text[0],
                          config.coord_year_text[1],
                          config.coord_year_text[2],
                          config.coord_year_text[3],
                          config.base_off_button_color, config.base_off_bg_button_color,
                          config.base_on_button_color, config.base_on_bg_button_color,
                          str(game_state.year) + " год, 23 мая", display.add_id(), display))

    map_buttons = []

    for index in range(config.quantity_buttons_map):
        map_buttons.append(
            Button(
                config.coordinates_button_map[0] + config.distance_button_map[0] * index + config.size_button_map[0],
                config.coordinates_button_map[1] + config.distance_button_map[1] * index + config.size_button_map[1],
                config.coordinates_button_map[0] + config.distance_button_map[0] * index,
                config.coordinates_button_map[1] + config.distance_button_map[1] * index,
                config.base_off_button_color,
                config.base_off_bg_button_color,
                config.base_on_button_color,
                config.base_on_bg_button_color,
                config.texts_buttons_map[index],
                display.add_id(),
                display,
                name=config.texts_buttons_map[index]
            )
        )
    buttons += map_buttons
    new_hint = hint.Hint(-1, -1, config.base_off_button_color, config.base_off_bg_button_color,
                         "", display.add_id(), display)
    buttons.append(new_hint)

    noice = path_noice.Noice(display.add_id(), display)
    noice.display_object()

    buttons.append(noice)

    play_manager = manager.PlayManager(display, buttons, id_objects_in_main_menu, game_state)
    play_manager.hide()
    play_manager.hint = new_hint
    play_manager.id_cities = dict_cities
    play_manager.map_buttons = map_buttons

    return play_manager