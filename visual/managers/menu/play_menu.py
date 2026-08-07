import visual.managers.managers.play_manager as manager
import visual.components.noice as path_noice
import mainloop.game_states as game_states
import visual.components.hint as hint
import config

def get_menu(display, game_state:game_states.GameState):
    buttons = []


    id_objects_in_main_menu = []
    new_hint = hint.Hint(-1, -1, config.base_off_button_color, config.base_off_bg_button_color,
                         "", display.add_id(), display)
    buttons.append(new_hint)

    noice = path_noice.Noice(display.add_id(), display)
    noice.display_object()

    buttons.append(noice)

    play_manager = manager.PlayManager(display, buttons, id_objects_in_main_menu, game_state)
    play_manager.hide()
    play_manager.hint = new_hint

    return play_manager