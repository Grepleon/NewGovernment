from hints.int_to_str import int_to_str
from visual.components.button import Button
from visual.components.city import VisualObjectCity
import visual.menu_builder.managers.manager as base_manager
import mainloop.game_states as game_states
import config
import visual.components.text as text
from hints.rename_politicians import rename
from hints.colors.lite import lite
import visual.components.button as button
from visual.tools.maps.upload_map import upload_map
import datetime as dt
import visual.tools.maps.specific_ethnic_map as sem
from countries.inter_city.inter_to_str import inter_to_str
from visual.tools.events.check_events import CheckerEvents

class PlayManager(base_manager.Manager):
    def __init__(self, display, buttons, id_objects, game_state:game_states.GameState):
        super().__init__(display, buttons, id_objects)
        self.game_state = game_state
        self.hint = None
        self.flag_del = False
        self.id_cities:dict[str:VisualObjectCity] = []
        self.map_buttons:list[str:Button] = []
        self.selected_map = config.selected_map
        self.button_time:Button|None = None
        self.play = False
        self.additional_buttons_map:list[Button] = []
        self.info_text = None
        self.tools_texts = None
        self.tools_button = None
        self.game_event = None
        self.checker_events:CheckerEvents|None = None

    def check_cities(self):
        flag = False
        for name_city in self.id_cities:
            self.display.recolor(lite(self.id_cities[name_city].color, -120), name_city)

        for name_city in self.id_cities:
            city = self.id_cities[name_city]

            if city.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                flag = True
                self.hint.to_move(self.display.mouse_x, self.display.mouse_y)
                self.hint.rewrite_text(
                    city.country.name
                    + "\n" +
                    city.area.to_str()
                    + "\n" + "\n" +
                    city.city.to_str()
                    + "\n" + "\n" +
                    inter_to_str(city.country, city.area, city.city, self.game_state.selected_politician)
                )
                self.hint.recolor(lite(city.area.color, 40), lite(city.area.color, -120))
                area = city.area
                object_city = city
                country = city.country
                selected_city = city.city.name

                for name_area_in_county in country.areas:
                    area_in_country = country.areas[name_area_in_county]
                    for name_city_in_country in area_in_country.cities:
                        city_in_country = area_in_country.cities[name_city_in_country]
                        self.display.recolor(lite(self.id_cities[city_in_country.name].color, -100), city_in_country.name)

                for name_city_in_area in area.cities:
                    city_in_area = area.cities[name_city_in_area]
                    self.display.recolor(lite(self.id_cities[city_in_area.name].color, -60), city_in_area.name)

                self.display.recolor(lite(self.id_cities[name_city].color, -20), name_city)

        if not flag:
            self.hint.hide()
        else:
            self.hint.show()
            self.hint.display_object(7, 16)

    def check_map(self):
        for map_button in self.map_buttons:
            if map_button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if self.display.fast_left_button_pressed:
                    if (map_button.name not in self.game_state.nations or
                                config.specific_ethnic_map == self.selected_map or
                                        self.selected_map in self.game_state.nations):
                        self.selected_map = map_button.name
                        upload_map(self.selected_map, self.display, self.game_state, self.id_cities)

        for map_button in self.map_buttons:
            if map_button.on and map_button.name != self.selected_map:
                map_button.on = False

    def ethno_button_check(self):
        if config.specific_ethnic_map == self.selected_map or self.selected_map in self.game_state.nations:
            for _button in self.additional_buttons_map:
                _button.show()
        else:
            for _button in self.additional_buttons_map:
                _button.hide()

    def check_hints_events(self):
        if not self.game_event.on:
            return
        for i, event_button in enumerate(self.game_event.buttons):
            event_button:button.Button = event_button
            if event_button.into_mouse and self.game_event.hints_texts[i] != "":
                self.hint.rewrite_text(self.game_event.hints_texts[i])
                self.hint.recolor(config.base_off_button_color, config.base_off_bg_button_color)
                self.hint.show()
                self.hint.to_move(self.display.mouse_x, self.display.mouse_y)

    def check(self):
        self.play = self.button_time.on

        for _button in self.buttons:
            if _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if self.display.fast_left_button_pressed:
                    _button.mouse_clicked_object()

            _button.display_object()

        self.checker_events.check()

        self.check_cities()
        self.check_map()
        self.button_time.rewrite_text(self.game_state.year_to_str())
        if self.play:
            self.game_state.time += dt.timedelta(minutes=config.dtime)
            self.game_state.ticks += 1

        self.check_hints_events()
        self.ethno_button_check()



    def delete(self):
        for _button in self.buttons:
            _button.delete()

        for id_object in self.id_objects:
            self.display.delete(id_object)

    def hide(self):
        for _button in self.buttons:
            _button.hide()

        for id_object in self.id_objects:
            self.display.hide(id_object)

        if self.flag_del:
            self.buttons.pop(-1)
            for i in range(3):
                self.id_objects.pop(-1)
        self.flag_del = False

    def show_selected_politician(self):
        self.flag_del = True
        frame_picture = self.display.create_image(config.coordinates_selected_politician[0],
                                             config.coordinates_selected_politician[1],
                                             config.path_to_frame_picture)

        self.id_objects.append(frame_picture)
        self.buttons.append(text.Text(
            config.coordinates_selected_politician[0] + config.frame_size_add,
            config.coordinates_selected_politician[1] + config.frame_size_add + config.height_button_in_frame,
            config.coordinates_selected_politician[0] + config.frame_size_into[0] - config.frame_size_add,
            config.coordinates_selected_politician[1] + config.frame_size_into[1] - config.frame_size_add,
            config.base_off_button_color, config.dark_off_bg_button_color,
            rename(self.game_state.selected_politician.name), self.display.add_id(), self.display,
            self.game_state.selected_politician.name))


        try:
            self.id_objects.append(
                self.display.create_image(config.coordinates_selected_politician[0] + config.frame_size_add,
                                     config.coordinates_selected_politician[1] + config.frame_size_add,
                                     config.politicians_folder + self.game_state.selected_politician.name
                                          + config.small_flag + config.format_pictures))
            self.id_objects.append(
            self.display.create_image(config.coordinates_selected_politician[0] + config.frame_size_add,
                             config.coordinates_selected_politician[1] + config.frame_size_add,
                             config.politicians_folder + self.game_state.selected_politician.name
                                      + config.hover_flag + config.format_pictures))
        except Exception as e:
            self.id_objects.append(
                self.display.create_image(config.coordinates_selected_politician[0] + config.frame_size_add,
                                     config.coordinates_selected_politician[1] + config.frame_size_add,
                                     config.politicians_folder + config.default_name
                                          + config.small_flag + config.format_pictures))
            self.id_objects.append(
            self.display.create_image(config.coordinates_selected_politician[0] + config.frame_size_add,
                             config.coordinates_selected_politician[1] + config.frame_size_add,
                             config.politicians_folder + config.default_name
                                      + config.hover_flag + config.format_pictures))

    def show(self):
        self.map_buttons[0].on = True
        upload_map(config.selected_map, self.display, self.game_state, self.id_cities)
        self.show_selected_politician()
        for _button in self.buttons:
            _button.show()

        for id_object in self.id_objects:
            self.display.show(id_object)
