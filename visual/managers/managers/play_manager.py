import visual.components.base_object as base_object
import visual.managers.managers.manager as base_manager
import mainloop.game_states as game_states
import config
import visual.components.text as text
from hints.rename_politicians import rename

class PlayManager(base_manager.Manager):
    def __init__(self, display, buttons, id_objects, game_state:game_states.GameState):
        super().__init__(display, buttons, id_objects)
        self.game_state = game_state

    def check(self):
        for _button in self.buttons:
            if _button.mouse_into_object(self.display.mouse_x, self.display.mouse_y):
                if self.display.fast_left_button_pressed:
                    _button.mouse_clicked_object()
            _button.display_object()

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

    def show_selected_politician(self):
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
            rename(self.game_state.selected_politician.name)))


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
