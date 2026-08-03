import visual.managers.managers.manager as manager
import visual.components.noice as path_noice

def get_menu(display):
    buttons = []


    id_objects_in_main_menu = []


    noice = path_noice.Noice(display.add_id(), display)
    noice.display_object()

    buttons.append(noice)

    play_manager = manager.Manager(display, buttons, id_objects_in_main_menu)
    play_manager.hide()

    return play_manager