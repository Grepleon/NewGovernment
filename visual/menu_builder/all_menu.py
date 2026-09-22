import visual.menu_builder.managers.manager as manager
import visual.menu_builder.menu.main_menu as main_menu
import visual.menu_builder.menu.character_menu as character_menu
import visual.menu_builder.menu.play_menu as play_menu
from mainloop.game_states import GameState
from politicians.actions.carry_out_solution import carry_out_solutions

class AllMenu:
    def __init__(self, display, game_state):
        self.display = display
        self.game_state:GameState = game_state

        self.main_manager, self.main_button = main_menu.get_menu(display)
        self.character_manager, self.cancel_character_button, self.character_button = character_menu.get_menu(display,
                                                                                game_state.politicians, self.game_state)
        self.play_manager = play_menu.get_menu(display, self.game_state)

        self.manager_used: manager.Manager = self.main_manager


    def checker(self):
        for add_win in self.game_state.additional_windows:
            if add_win.check_activity():
                add_win.base_process()
                add_win.process()

        self.manager_used.check()
        self.manager_used.active()

        if self.manager_used is self.main_manager:
            if self.main_button.on:
                self.main_button.on = False
                self.manager_used.hide()
                self.character_manager.show()
                self.manager_used = self.character_manager

        elif self.manager_used is self.character_manager:
            if self.cancel_character_button.on:
                self.cancel_character_button.on = False
                self.manager_used.hide()
                self.main_manager.show()
                self.manager_used = self.main_manager

            if self.character_button.on:
                self.character_button.on = False
                self.manager_used.hide()
                self.play_manager.show()
                self.manager_used = self.play_manager
                self.game_state.statistics.add_selected_politician(self.game_state.selected_politician.name,
                                                                   self.game_state.selected_politician)
                carry_out_solutions("провести большое интервью", self.display, self.game_state,
                                    self.game_state.selected_politician)

        self.display.fast_left_button_pressed = False
        self.display.tact += 1
        self.display.update_fun(self.checker, 20)




