from visual.display import Display
import config
from mainloop.game_states import GameState
import visual.components.text as text

from visual.tools.maps.regional_map import upload_regional_map
from visual.tools.maps.political_map import upload_political_map
from visual.tools.maps.demographic_map import upload_demographic_map
from visual.tools.maps.economic_map import upload_economic_map
from visual.tools.maps.gdp_per_capita_map import upload_gdp_per_capita_map

map_tools:dict = {
    "Областная карта": upload_regional_map,
    "Политическая карта": upload_political_map,
    "Демографическая карта": upload_demographic_map,
    "Экономическая карта": upload_economic_map,
    "Карта ВВП на д.н.": upload_gdp_per_capita_map
}

def upload_map(name_map, display:Display, game_state:GameState, area_cities):
    map_tools[name_map](display, game_state, area_cities)