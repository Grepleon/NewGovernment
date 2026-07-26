import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button
import visual.managers.manager as manager

class AllMenu:
    def __init__(self, display):
        self.display = display

        buttons = []

        main_button_coordinates = config.main_button_coordinates
        self.main_button = button.Button(config.main_button_coordinates[0], config.main_button_coordinates[1],
                                    config.main_button_coordinates[2], config.main_button_coordinates[3],
                                    config.base_off_button_color, config.base_off_bg_button_color,
                                    config.base_on_button_color, config.base_on_bg_button_color,
                                    config.main_button_text, display.add_id(), display)
        buttons.append(self.main_button)

        self.main_button.display_object()

        id_objects_in_main_menu = []

        main_image_coordinates = config.coordinates_picture_into_main
        main_image = display.create_image(main_image_coordinates[0], main_image_coordinates[1],
                                          config.path_to_picture_into_main)

        id_objects_in_main_menu.append(main_image)

        self.main_manager = manager.Manager(display, buttons, id_objects_in_main_menu)
        self.manager_used: manager.Manager = self.main_manager

        self.main_character = manager.Manager(display, [], [])

    def checker(self):
        self.manager_used.check()
        if self.manager_used is self.main_manager and self.main_button.on:
            self.manager_used.hide()
            self.manager_used = self.main_character
        self.display.update_fun(self.checker, 100)

