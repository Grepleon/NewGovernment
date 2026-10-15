import countries.cities.location as loc
import countries.cities.infrastructure.roads as roads
import countries.cities.infrastructure.buildings as buildings
import hints.int_to_str as its
import politicians.nation.ethnic_group as eg
from countries.cities.geography import Geography
from politicians.policy.political_compass import PoliticalCompass
from politicians.politician import Politician
from gameloop.resources.base import Resources

class City:
    def __init__(self, name, mayor, location, infrastructure, peoples, budget, nations,
                 products, geography, popular_ideas, full_name, resources):
        self.name:str = name
        self.mayor:str = mayor
        self.location:loc.Location = location
        self.infrastructure: list[buildings.Building] = infrastructure
        self.peoples:int = peoples # указывается в тысячах
        self.budget:int = budget # бюджет
        self.nations:dict[str:eg.EthnicGroup] = nations
        self.products = products
        self.geography:Geography = geography
        self.popular_ideas:PoliticalCompass = popular_ideas
        self.full_name = full_name
        self.resources:dict[str: Resources] = resources

    def to_str(self):
        return (f"Город {self.name}:"
                f"\nМэр: {self.mayor}"
                f"\nБюджет: {its.int_to_str(self.budget)}"
                f"\nЭтнически группы:"
                f"\n- {"\n- ".join([nation.to_str() for nation in self.nations])}"
                f"\nНаселение: {its.int_to_str(self.peoples * 1000)}"
                f"\nПроизведено товаров и услуг: {its.int_to_str(self.products)}"
                f"\nГеография: {self.geography.to_str()}"
                f"\nПопулярные взгляды: {self.popular_ideas.to_str_name()}"
                )

    def get_sum_res(self):
        return sum([
            self.resources[res].explored_quantity for res in self.resources
        ])

    def get_res(self):
        return f"Ресурсы:\n{"\n".join([
            self.resources[res].to_str() for res in self.resources if
            self.resources[res].explored_quantity != 0 or self.resources[res].extracted != 0
        ])}"

    def vote(self, politician: Politician):
        x1 = self.popular_ideas.left_right
        x2 = politician.political_compass.left_right
        y1 = self.popular_ideas.freedom
        y2 = politician.political_compass.freedom
        distance = ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
        fine_distance = distance ** 1.5
        return max(
            politician.popularity.peoples_total() *
            politician.reputation ** 1.5
            * (100 - fine_distance) / 100 *
            politician.popularity.get_pop_city(self.full_name),
            0
        )
