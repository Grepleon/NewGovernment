import countries.cities.infrastructure.buildings as b

class Road(b.Building):
    def __init__(self, name, cost):
        super().__init__(name, "road", cost, 0)
