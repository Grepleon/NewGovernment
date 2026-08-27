from visual.display import Display
from visual.components.game_event import GameEvent
from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its
import random

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

        for politician_name in self.game_state.politicians:
            politician = self.game_state.politicians[politician_name]
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
                    point += city.vote(politician)
            if self.game_state.politicians[country.ruler].name == politician.name:
                point *= country.falsifications["ruler"]
            if self.game_state.politicians[country.ruler].name_party == politician.name_party:
                point *= country.falsifications["ruling_party"]
            sum_points += point
            points[politician.name] = int(point)

            print(politician.name, "-", its(point))

        for politician in candidates:
            point = points[politician.name]
            re_candidates.append(f"{politician.name} - {round(point / sum_points * 100, 2)}%")

        return re_candidates

    def check(self):
        if not self.game_event.on:
            if self.game_state.get_day() == "00:00 1":
                self.get_salary()
            if self.game_state.get_month() == "00:00 1.1":
                self.game_event.show()
                self.game_event.rewrite(
                    f"С новым {self.game_state.get_year()} годом!",
                    ["С новым годом!", "", "", "", ""],
                ["Нажмите, чтобы продолжить играть", "", "", "", ""]
                )
                self.game_event.show_buttons = 1
            for name_country in self.game_state.countries:
                country = self.game_state.countries[name_country]
                if country.next_vote == self.game_state.get_str_year():
                    candidates = self.voted(country)
                    self.game_event.rewrite(
                        f"Выборы в государстве {country.name}\n"
                        f"Кандидаты: \n{"\n".join(candidates)}",
                        ["Поздравляю нового правителя!", "Выборы точно были фальсифицированы...", "", "", ""],
                        ["", "", "", "", ""]
                    )
                    self.game_event.show_buttons = 2
                    self.game_event.show()

