import visual.menu_builder.managers.manager as manager
import visual.menu_builder.menu.main_menu as main_menu
import visual.menu_builder.menu.character_menu as character_menu
import visual.menu_builder.menu.play_menu as play_menu

class AllMenu:
    def __init__(self, display, game_state):
        self.display = display
        self.game_state = game_state

        self.main_manager, self.main_button = main_menu.get_menu(display)
        self.character_manager, self.cancel_character_button, self.character_button = character_menu.get_menu(display,
                                                                                game_state.politicians, self.game_state)
        self.play_manager = play_menu.get_menu(display, self.game_state)

        self.manager_used: manager.Manager = self.main_manager


    def checker(self):
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

        self.display.fast_left_button_pressed = False
        self.display.tact += 1
        self.display.update_fun(self.checker, 20)




