from visual.display import Display
import config
from mainloop.game_states import GameState
import visual.components.text as text

from visual.tools.maps.regional_map import upload_regional_map
from visual.tools.maps.political_map import upload_political_map

map_tools:dict = {
    "Областная карта": upload_regional_map,
    "Политическая карта": upload_political_map
}

def upload_map(name_map, display:Display, game_state:GameState, area_cities):
    map_tools[name_map](display, game_state, area_cities)