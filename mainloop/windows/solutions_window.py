from visual.components.base_object import BaseObject as GameObject
from mainloop.windows.additional_windows import AdditionalWindow
from visual.components.hint import Hint
from visual.display import Display
from visual.components.base_object import BaseObject
from visual.components.button import Button
from hints.enters import space
from politicians.politician import Politician
from politicians.actions.carry_out_solution import carry_out_solutions

class SolutionWindow(AdditionalWindow):
    hint:Hint|None = None
    last_button:Button|None = None

    def get_sum_polh(self):
        sum_polh = 0
        for component in self.components:
            if type(component) == Button and component != self.last_button:
                if component.on:
                    sum_polh += component.info.get("polh")
        return sum_polh

    def check_last_button(self):
        selected_politician: Politician = self.game_state.selected_politician

        if self.last_button.into_mouse:
            self.hint.show()
            self.hint.rewrite_text(space(
                f"Будет затрачено {self.get_sum_polh()} полит. часов.\n"
                f"Вам {f"не хватает {self.get_sum_polh() - selected_politician.political_hour 
                }" if selected_politician.political_hour < self.get_sum_polh() else
                "хватает"} полит. часов.",
                20, 25))
            self.hint.to_move(
                self.display.mouse_x,
                self.display.mouse_y
            )
        if self.last_button.on:
            if selected_politician.political_hour >= self.get_sum_polh():
                selected_politician.political_hour -= self.get_sum_polh()
                self.game_state.statistics.spent_polh += self.get_sum_polh()
                for component in self.components:
                    if type(component) == Button and component != self.last_button:
                        if component.on:
                            self.carry_out(component.info["name"])


            self.display.switch_window(self.display.main_window)
            self.display.destroy_window(self.name_window)
            return True
        return False

    def carry_out(self, name):
        carry_out_solutions(name, self.display, self.game_state, self.game_state.selected_politician)

    def process(self):
        if self.check_activity():
            self.display.switch_window(self.name_window)
            self.hint.hide()

            for component in self.components:
                if type(component) == Button:
                    component:Button = component
                    if component.into_mouse:
                        self.hint.show()
                        self.hint.rewrite_text(space(component.name, 20, 25))
                        self.hint.to_move(
                            self.display.mouse_x,
                            self.display.mouse_y
                        )
            if self.check_last_button():
                return

        self.display.switch_window(self.display.main_window)