import visual.components.base_object as base_object
from visual.components.hint import Hint
import visual.menu_builder.managers.manager as base_manager
import mainloop.game_states as game_states
import config
import visual.components.text as text
from hints.rename_politicians import rename
from hints.lite import lite

class PlayManager(base_manager.Manager):
    def __init__(self, display, buttons, id_objects, game_state:game_states.GameState):
        super().__init__(display, buttons, id_objects)
        self.game_state = game_state
        self.hint = None
        self.flag_del = False
        self.id_cities = []

    def check(self):
        flag = False
        for _button in self.buttons:
            if _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if _button in self.id_cities:
                    flag = True
                    self.hint.to_move(self.display.mouse_x, self.display.mouse_y)
                    self.hint.rewrite_text(_button.area.to_str() + "\n" + "\n" + _button.city.to_str())
                    self.hint.recolor(lite(_button.area.color, 40), lite(_button.area.color, -120))
                if self.display.fast_left_button_pressed:
                    _button.mouse_clicked_object()

            _button.display_object()

        if not flag:
            self.hint.hide()
        else:
            self.hint.show()
            self.hint.display_object(7)

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
        self.show_selected_politician()
        for _button in self.buttons:
            _button.show()

        for id_object in self.id_objects:
            self.display.show(id_object)
