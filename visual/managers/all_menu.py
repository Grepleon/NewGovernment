import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button
import visual.managers.manager as manager
import visual.managers.menu.main_menu as main_menu
import visual.managers.menu.character_menu as character_menu

class AllMenu:
    def __init__(self, display):
        self.display = display

        self.main_manager, self.main_button = main_menu.get_menu(display)
        self.character_manager, self.cancel_character_button, self.main_button = character_menu.get_menu(display)

        self.manager_used: manager.Manager = self.main_manager


    def checker(self):
        self.manager_used.check()
        if self.manager_used is self.main_manager and self.main_button.on:
            print(1)
            self.manager_used.hide()
            self.character_manager.show()
            self.manager_used = self.character_manager

        elif self.manager_used is self.character_manager and self.cancel_character_button.on:
            print(2)
            self.manager_used.hide()
            self.main_manager.show()
            self.manager_used = self.main_manager

        self.display.fast_left_button_pressed = False
        self.display.update_fun(self.checker, 100)

