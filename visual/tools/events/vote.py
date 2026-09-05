from visual.display import Display
from visual.components.game_event import GameEvent
from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its
import random


def voted(self, country, job):
    candidates = []
    re_candidates = []
    points = {}
    max_points = 0
    winner = None

    for politician_name in self.game_state.politicians:
        politician = self.game_state.politicians[politician_name]
        if country.name in politician.citizenship and not politician.blocked[job]:
            wish = (politician.position.importance * politician.popularity.peoples_total() *
                    politician.reputation ** 1.5 * politician.ambitions)
            print(politician.participating[job])
            if (wish > 30_000_000 or
                wish > 15_000_000 and random.randint(1, 2) == 1
                or politician.participating[job]
            ):
                candidates.append(politician)
                points[politician_name] = 0


            print(politician_name, "-", its(wish))

    sum_points = 0
    sum_fair_points = 0
    max_fair_points = 0
    for politician in candidates:
        point = 0
        for area_name in country.areas:
            area = country.areas[area_name]
            for city_name in area.cities:
                city = area.cities[city_name]
                first_points = city.vote(politician)
                max_fair_points += 100000
                sum_fair_points += first_points
                point += first_points * city.peoples / 100
        if self.game_state.politicians[country.ruler].name == politician.name:
            point *= country.falsifications["ruler"]
        if self.game_state.politicians[country.ruler].name_party == politician.name_party:
            point *= country.falsifications["ruling_party"]
        point /= 100000
        point **= 5
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
        lens = 50
        re_candidates.append(f"{'|' * int(point / sum_points * lens)}"
                             f"{'.' * int(lens - point / sum_points * lens)}"
                             f"")

    self.game_state.statistics.check_votes(job, winner, max_points,
                                           self.game_state.selected_politician.name)
    turnout = sum_fair_points / max_fair_points / 2 + 0.50
    return re_candidates, winner, turnout