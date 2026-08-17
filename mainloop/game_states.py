import politicians.politician as politician
import countries.country as country
import politicians.nation.base_nation as bn
from statistics import Statistics
import datetime as dt
import pytz
from babel.dates import format_datetime

class GameState:
    def __init__(self, year, ticks, selected_politician:politician.Politician|None,
                 politicians:list[politician.Politician],
                 countries: dict[str:country.Country], nations: dict[str:bn.Nation], statistics:Statistics):
        self.time:dt.datetime = year
        self.ticks = ticks
        self.selected_politician:politician.Politician = selected_politician
        self.politicians:list[politician.Politician] = politicians
        self.countries: dict[str:country.Country] = countries
        self.nations: dict[str:bn.Nation] = nations
        self.statistics:Statistics = statistics

    def year_to_str(self):
        return format_datetime(self.time, "HH:00, d MMMM, y год", locale='ru')

    def get_str_year(self):
        return format_datetime(self.time, "HH:mm d.M.y", locale='ru')