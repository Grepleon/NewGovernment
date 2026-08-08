import politicians.politician as politician
import countries.country as country


class GameState:
    def __init__(self, year, selected_politician:politician.Politician, politicians:list[politician.Politician],
                 countries: dict[str:country.Country]):
        self.year = year
        self.selected_politician = selected_politician
        self.politicians = politicians
        self.countries = countries