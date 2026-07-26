import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button
import visual.managers.manager as manager

def get_menu(display):
    buttons = []

    main_button = button.Button(config.character_button_coordinates[0], config.character_button_coordinates[1],
                                     config.character_button_coordinates[2], config.character_button_coordinates[3],
                                     config.base_off_button_color, config.base_off_bg_button_color,
                                     config.base_on_button_color, config.base_on_bg_button_color,
                                     config.character_button_text, display.add_id(), display)


    cancel_button = button.Button(config.cancel_character_button_coordinates[0],
                                  config.cancel_character_button_coordinates[1],
                                  config.cancel_character_button_coordinates[2],
                                  config.cancel_character_button_coordinates[3],
                                  config.cancel_off_button_color, config.cancel_off_bg_button_color,
                                  config.cancel_on_button_color, config.cancel_on_bg_button_color,
                                  config.cancel_charactor_button_text, display.add_id(), display)

    buttons.append(main_button)
    buttons.append(cancel_button)

    main_button.display_object()

    id_objects = []

    # main_image_coordinates = config.coordinates_picture_into_main
    # main_image = display.create_image(main_image_coordinates[0], main_image_coordinates[1],
    #                                   config.path_to_picture_into_main)
    #
    # id_objects.append(main_image)

    character_menu = manager.Manager(display, buttons, id_objects)
    character_menu.hide()

    return character_menu, cancel_button, main_button