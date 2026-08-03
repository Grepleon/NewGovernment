import config
import visual.components.button as button
import visual.managers.managers.character_manager as manager
import visual.components.noice as path_noice
import visual.components.hint as hint

def rename(val:str):
    return " ".join(val.split()[:2])

def get_menu(display, politicians):
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
    for index_frame in range(config.quantity_frames):
        frame_picture = display.create_image(config.coordinates_frame_picture[index_frame * 2 + 0],
                                                     config.coordinates_frame_picture[index_frame * 2 + 1],
                                                     config.path_to_frame_picture)

        id_objects.append(frame_picture)
        buttons.append(button.Button(
    config.coordinates_frame_picture[index_frame * 2 + 0] + config.frame_size_add,
    config.coordinates_frame_picture[index_frame * 2 + 1] + config.frame_size_add + config.height_button_in_frame,
    config.coordinates_frame_picture[index_frame * 2 + 0] + config.frame_size_into[0] - config.frame_size_add,
    config.coordinates_frame_picture[index_frame * 2 + 1] + config.frame_size_into[1] - config.frame_size_add,
                              config.base_off_button_color, config.dark_off_bg_button_color,
                              config.base_on_button_color, config.base_on_bg_button_color,
                              rename(config.names_politicians[index_frame]), display.add_id(), display,
        config.names_politicians[index_frame]))

        try:
            id_objects.append(
                display.create_image(config.coordinates_frame_picture[index_frame * 2 + 0] + config.frame_size_add,
                                     config.coordinates_frame_picture[index_frame * 2 + 1] + config.frame_size_add,
                                     config.politicians_folder + config.names_politicians[
                                         index_frame] + config.small_flag + config.format_pictures))
            id_objects.append(
        display.create_image(config.coordinates_frame_picture[index_frame * 2 + 0] + config.frame_size_add,
                             config.coordinates_frame_picture[index_frame * 2 + 1] + config.frame_size_add,
                             config.politicians_folder + config.names_politicians[
                                 index_frame] + config.hover_flag + config.format_pictures))
        except Exception as e:
            id_objects.append(
                display.create_image(config.coordinates_frame_picture[index_frame * 2 + 0] + config.frame_size_add,
                                     config.coordinates_frame_picture[index_frame * 2 + 1] + config.frame_size_add,
                                     config.politicians_folder + config.default_name + config.small_flag + config.format_pictures))
            id_objects.append(
                display.create_image(config.coordinates_frame_picture[index_frame * 2 + 0] + config.frame_size_add,
                                     config.coordinates_frame_picture[index_frame * 2 + 1] + config.frame_size_add,
                                     config.politicians_folder + config.default_name + config.hover_flag + config.format_pictures))

    new_hint = hint.Hint(-1, -1, config.base_off_button_color, config.base_off_bg_button_color,
                         "", display.add_id(), display)
    buttons.append(new_hint)

    noice = path_noice.Noice(display.add_id(), display)
    noice.display_object()

    buttons.append(noice)

    character_menu = manager.CharacterManager(display, buttons, id_objects, politicians)
    character_menu.hide()

    return character_menu, cancel_button, main_button