import config
import visual.components.button as button
import visual.menu_builder.managers.manager as manager
import visual.components.noice as path_noice
import visual.components.game_event as ge

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

    test_event = ge.GameEvent(50, 50, 1150, 550, 10, 4, 50, ["Тест-1", "тест-2", "Сюда жми", "Тест-4"], "#00ff00", "#003300", "#00ff33", "#006600", "Супер ивент жми куда \n хочешь уу шесть семь", "СУПЕР", display)
    buttons += test_event.buttons
    buttons.append(test_event)

    noice = path_noice.Noice(display.add_id(), display)
    noice.display_object()

    buttons.append(noice)

    return manager.Manager(display, buttons, id_objects_in_main_menu), main_button