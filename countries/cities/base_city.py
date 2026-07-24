import countries.cities.location as loc
import countries.cities.infrastructure.roads as roads
import countries.cities.infrastructure.buildings as buildings

class City:
    def __init__(self, name, mayor, location, infrastructure, peoples, budget):
        self.name:str = name
        self.mayor:str = mayor
        self.location:loc.Location = location
        self.infrastructure: list[buildings.Building] = infrastructure
        self.peoples:int = peoples # указывается в тысячах
        self.budget:int = budget