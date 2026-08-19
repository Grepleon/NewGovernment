import countries.cities.base_city as bc
from hints.int_to_str import int_to_str as its

class Area:
    def __init__(self, name, cities, governor, costs, budget, autonomy, color="#ffffff"):
        self.name = name
        self.cities: dict[str:bc.City] = cities
        self.governor:str = governor
        self.budget = budget
        self.costs:dict[str:int] = costs
        self.color = color
        self.autonomy = autonomy

    def to_str(self):
        return (f"{self.name}:"
                f"\nГубернатор: {self.governor}"
                f"\nБюджет: {its(self.budget)}"
                f"\nНаселение: {its(sum([self.cities[city].peoples for city in self.cities]) * 1000)}"
                f"\nАвтономность: {self.autonomy}%")