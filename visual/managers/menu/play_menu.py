import visual.managers.managers.play_manager as manager
import visual.components.noice as path_noice
import mainloop.game_states as game_states

def get_menu(display, game_state:game_states.GameState):
    buttons = []


    id_objects_in_main_menu = []


    noice = path_noice.Noice(display.add_id(), display)
    noice.display_object()

    buttons.append(noice)

    play_manager = manager.PlayManager(display, buttons, id_objects_in_main_menu, game_state)
    play_manager.hide()

    return play_manager