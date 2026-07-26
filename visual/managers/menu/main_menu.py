import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button
import visual.managers.manager as manager
import visual.components.noice as path_noice

def get_menu(display):
    buttons = []

    main_button = button.Button(config.main_button_coordinates[0], config.main_button_coordinates[1],
                                     config.main_button_coordinates[2], config.main_button_coordinates[3],
                                     config.base_off_button_color, config.base_off_bg_button_color,
                                     config.base_on_button_color, config.base_on_bg_button_color,
                                     config.main_button_text, display.add_id(), display)
    buttons.append(main_button)

    main_button.display_object()

    id_objects_in_main_menu = []

    main_image_coordinates = config.coordinates_picture_into_main
    main_image = display.create_image(main_image_coordinates[0], main_image_coordinates[1],
                                      config.path_to_picture_into_main)

    id_objects_in_main_menu.append(main_image)

    noice = path_noice.Noice(display.add_id(), display)
    noice.display_object()

    buttons.append(noice)

    return manager.Manager(display, buttons, id_objects_in_main_menu), main_button