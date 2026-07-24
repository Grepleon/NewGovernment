import countries.cities.base_city as bc

class Area:
    def __init__(self, name, cities, governor, costs, budget):
        self.name = name
        self.cities: dict[str:bc.City] = cities
        self.governor:str = governor
        self.budget = budget
        self.costs:dict[str:int] = costs
