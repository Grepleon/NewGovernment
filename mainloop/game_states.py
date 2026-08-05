import politicians.politician as politician

class GameState:
    def __init__(self, year, selected_politician:politician.Politician, politicians:list[politician.Politician]):
        self.year = year
        self.selected_politician = selected_politician
        self.politicians = politicians