import countries.cities.location as loc
import countries.cities.infrastructure.roads as roads
import countries.cities.infrastructure.buildings as buildings
import hints.int_to_str as its
import politicians.nation.ethnic_group as eg
from countries.cities.geography import Geography

class City:
    def __init__(self, name, mayor, location, infrastructure, peoples, budget, nations,
                 products, geography):
        self.name:str = name
        self.mayor:str = mayor
        self.location:loc.Location = location
        self.infrastructure: list[buildings.Building] = infrastructure
        self.peoples:int = peoples # указывается в тысячах
        self.budget:int = budget # бюджет
        self.nations:dict[str:eg.EthnicGroup] = nations
        self.products = products
        self.geography:Geography = geography

    def to_str(self):
        return (f"Город {self.name}:"
                f"\nМэр: {self.mayor}"
                f"\nБюджет: {its.int_to_str(self.budget)}"
                f"\nЭтнически группы:"
                f"\n- {"\n- ".join([nation.to_str() for nation in self.nations])}"
                f"\nНаселение: {its.int_to_str(self.peoples * 1000)}"
                f"\nПроизведено товаров и услуг: {its.int_to_str(self.products)}"
                )
