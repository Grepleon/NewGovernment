import os
import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button
import visual.manager as manager

def create_politicians() -> dict[str:path_politician.Politician]:
    politicians = variable_characters()

    for politician in politicians:
        data_politician = politicians[politician]
        data_politician.start()

    return politicians


display = visual.mainloop.Display(config.width, config.height)

buttons = []

main_button_coordinates = config.main_button_coordinates
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

main_manager = manager.Manager(display, buttons, id_objects_in_main_menu)
manager_w:manager.Manager = main_manager

def checker():
    global manager_w
    manager_w.check()
    if main_button.on:
        manager_w.delete()
        manager_w = manager.Manager(display, [], [])
    display.update_fun(checker, 100)


checker()

display.end()
