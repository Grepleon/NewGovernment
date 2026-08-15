import politicians.politician as politician
import countries.country as country
import politicians.nation.base_nation as bn

class GameState:
    def __init__(self, year, selected_politician:politician.Politician, politicians:list[politician.Politician],
                 countries: dict[str:country.Country], nations: dict[str:bn.Nation]):
        self.year = year
        self.selected_politician = selected_politician
        self.politicians = politicians
        self.countries = countries
        self.nations = nations