import countries.cities.base_city as bc
from hints.int_to_str import int_to_str as its

class Area:
    def __init__(self, name, cities, governor, costs, budget):
        self.name = name
        self.cities: dict[str:bc.City] = cities
        self.governor:str = governor
        self.budget = budget
        self.costs:dict[str:int] = costs

    def to_str(self):
        return (f"{self.name}:"
                f"\nгорода: \n- {"\n- ".join([name for name in self.cities])}"
                f"\nбюджет: {its(self.budget)}")