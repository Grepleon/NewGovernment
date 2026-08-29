from visual.display import Display
from visual.components.game_event import GameEvent
from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its
import random


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
            politician.money += politician.position.get_money()

    def voted(self, country):
        candidates = []
        re_candidates = []
        points = {}
        max_points = 0
        winner = None

        for politician_name in self.game_state.politicians:
            politician = self.game_state.politicians[politician_name]
            if country.name in politician.citizenship:
                wish = (politician.position.importance * politician.popularity.peoples_total() *
                        politician.reputation ** 1.5 * politician.ambitions)
                if wish > 30_000_000: #100% идет
                    candidates.append(politician)
                    points[politician_name] = 0
                elif wish > 15_000_000 and random.randint(1, 2) == 1: #50 на 50
                    candidates.append(politician)
                    points[politician_name] = 0


                print(politician_name, "-", its(wish))

        sum_points = 0
        for politician in candidates:
            point = 0
            for area_name in country.areas:
                area = country.areas[area_name]
                for city_name in area.cities:
                    city = area.cities[city_name]
                    point += city.vote(politician) * city.peoples / 100
            if self.game_state.politicians[country.ruler].name == politician.name:
                point *= country.falsifications["ruler"]
            if self.game_state.politicians[country.ruler].name_party == politician.name_party:
                point *= country.falsifications["ruling_party"]
            sum_points += point
            points[politician.name] = int(point)

            print(politician.name, "-", its(point))

        for politician in candidates:
            point = points[politician.name]
            if max_points < point:
                winner = politician.name
                max_points = point
            print(politician.name, ':', its(point))
            re_candidates.append(f"{politician.name} - {round(point / sum_points * 100, 2)}%")

        return re_candidates, winner

    def check(self):
        if not self.game_event.on:
            if self.game_state.get_day() == "00:00 1":
                self.get_salary()
            if self.game_state.get_month() == "00:00 1.1":
                self.game_event.show()
                self.game_event.rewrite(
                    f"С новым {self.game_state.get_year()} годом!",
                    ["С новым годом!", "", "", "", ""],
                ["Нажмите, чтобы продолжить играть", "", "", "", ""],
                    [passed, passed, passed, passed, passed]
                )
                self.game_event.show_buttons = 1
            for name_country in self.game_state.countries:
                country = self.game_state.countries[name_country]
                if country.next_vote == self.game_state.get_str_year():
                    candidates, winner = self.voted(country)
                    self.game_event.rewrite(
                        f"Выборы в государстве {country.name}\n"
                        f"Кандидаты: \n{"\n".join(candidates)}"
                        f"\nНовым правителем стал {winner}!",
                        ["Поздравляю нового правителя!",
                         "Выборы точно были фальсифицированы...",
                         "Промолчать", "", ""],
                        [
                         "Вас поддержат олигархия, и вы будете популярны \nсреди голосовавших за нового правителя",
                         "Вас будут призирать олигархия, но среди противников\nнового правителя вы будете популярны",
                         "Ничего не произойдет", "", ""],
                        [support_ruler, support_opposition, passed, passed, passed]
                    )
                    self.game_event.show_buttons = 3
                    self.game_event.show()

