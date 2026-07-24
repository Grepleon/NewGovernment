import countries.cities.infrastructure.buildings as b

class Road(b.Building):
    def __init__(self, name, type, cost):
        super().__init__(name, type, cost, 0)
