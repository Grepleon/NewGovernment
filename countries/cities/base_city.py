import countries.cities.location as loc
import countries.cities.infrastructure.roads as roads
import countries.cities.infrastructure.buildings as buildings
import hints.int_to_str as its

class City:
    def __init__(self, name, mayor, location, infrastructure, peoples, budget):
        self.name:str = name
        self.mayor:str = mayor
        self.location:loc.Location = location
        self.infrastructure: list[buildings.Building] = infrastructure
        self.peoples:int = peoples # указывается в тысячах
        self.budget:int = budget # бюджет

    def to_str(self):
        return (f"Город {self.name}:"
                f"\nМэр: {self.mayor}"
                f"\nНаселение: {its.int_to_str(self.peoples * 1000)}"
                f"\nБюджет: {its.int_to_str(self.budget)}")