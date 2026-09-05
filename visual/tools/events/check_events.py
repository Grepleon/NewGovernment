from visual.display import Display
from visual.components.game_event import GameEvent
from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its
import random
from visual.tools.events.vote import voted

def passed(null):
    pass

def support_opposition(game_state:GameState):
    game_state.selected_politician.popularity.for_peoples(5)
    game_state.selected_politician.support.oligarchs = max(game_state.selected_politician.support.oligarchs - 3, 0)

def support_ruler(game_state:GameState):
    game_state.selected_politician.popularity.for_in_power(2)
    game_state.selected_politician.support.oligarchs = min(game_state.selected_politician.support.oligarchs + 5, 100)


class CheckerEvents:
    def __init__(self, display, game_state, game_event):
        self.display:Display = display
        self.game_state:GameState = game_state
        self.game_event:GameEvent = game_event

    def get_salary(self):
        for name_politician in self.game_state.politicians:
            politician = self.game_state.politicians[name_politician]
            politician.new_month()

    def get_new_year(self):
        for name_politician in self.game_state.politicians:
            politician = self.game_state.politicians[name_politician]
            politician.new_year()

    def check(self):
        if not self.game_event.on:
            if self.game_state.get_day() == "00:00 1":
                self.get_salary()
            if self.game_state.get_month() == "00:00 1.1":
                self.get_new_year()
                self.game_event.show()
                self.game_event.rewrite(
                    f">> С новым {self.game_state.get_year()} годом!",
                    ["С новым годом!", "", "", "", ""],
                ["Нажмите, чтобы продолжить играть", "", "", "", ""],
                    [passed, passed, passed, passed, passed],
                    "Новый год"
                )
                self.game_event.show_buttons = 1
            for name_country in self.game_state.countries:
                country = self.game_state.countries[name_country]
                if country.next_vote == self.game_state.get_str_year():
                    candidates, winner, turnout = voted(self, country, "ruler")
                    self.game_event.rewrite(
                        f">> Выборы в государстве {country.name}\n"
                        f"Явка: {round(turnout * 100, 2)}%\n\n"
                        f"Кандидаты: \n{"\n".join(candidates)}"
                        f"\n\nНовым правителем стал:\n{winner.upper()}!",
                        ["Поздравляю нового правителя!",
                         "Выборы точно были фальсифицированы...",
                         "Промолчать", "", ""],
                        [
                         "Вас поддержат олигархия, и вы будете популярны \nсреди голосовавших за нового правителя",
                         "Вас будут призирать олигархия, но среди противников\nнового правителя вы будете популярны",
                         "Ничего не произойдет", "", ""],
                        [support_ruler, support_opposition, passed, passed, passed],
                        "Выборы правителя"
                    )
                    self.game_event.show_buttons = 3
                    self.game_event.show()

