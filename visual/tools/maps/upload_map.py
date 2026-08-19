from visual.display import Display
import config
from mainloop.game_states import GameState
import visual.components.text as text

from visual.tools.maps.regional_map import upload_regional_map
from visual.tools.maps.political_map import upload_political_map
from visual.tools.maps.demographic_map import upload_demographic_map
from visual.tools.maps.economic_map import upload_economic_map
from visual.tools.maps.gdp_per_capita_map import upload_gdp_per_capita_map
from visual.tools.maps.ethnic_map import upload_ethnic_map
from visual.tools.maps.physical_map import upload_physical_map
from visual.tools.maps.climate_map import upload_climate_map
from visual.tools.maps.climate_map import upload_climate_map
from visual.tools.maps.populist_map import upload_populist_map
from visual.tools.maps.autonomy_map import upload_autonomy_map
from visual.tools.maps.specific_ethnic_map import upload_ethnic_map as upload_specific_ethnic_map

map_tools:dict = {
    "Областная карта": upload_regional_map,
    "Политическая карта": upload_political_map,
    "Физическая карта": upload_physical_map,
    "Демографическая карта": upload_demographic_map,
    "Экономическая карта": upload_economic_map,
    "Карта ВВП на д.н.": upload_gdp_per_capita_map,
    "Этническая карта": upload_ethnic_map,
    "Климатическая карта": upload_climate_map,
    "Популистская карта": upload_populist_map,
    "Карта автономности": upload_autonomy_map,
}

def upload_map(name_map, display:Display, game_state:GameState, area_cities):
    game_state.statistics.maps_choose[name_map] = game_state.statistics.maps_choose.get(name_map, 0) + 1
    if name_map in game_state.nations:
        upload_specific_ethnic_map(display, game_state, area_cities, name_map)
        return
    map_tools[name_map](display, game_state, area_cities)
