import saves
import os
import politicians.politician as pol, politicians.policy.political_compass as pol_com
import politicians.policy.str_to_characteristic as str_to_ch
import politicians.policy.str_to_job_title as str_to_pos
import politicians.policy.popularity.popularity_indicator as pi
import politicians.policy.popularity.support as support
import countries.country as country
import countries.areas.base_area as ba
import countries.cities.base_city as bc
from countries.cities.location import Location
import countries.cities.infrastructure.buildings as buildings
import politicians.nation.base_nationality as bn
from politicians.nation.base_nation import Nation
from politicians.nation.ethnic_group import EthnicGroup

def get_country_json_file(val:str):
    return val + '/' + val + '.json'

def c_add_to_cities(_file:str, area:str, key, val) -> dict[str:bc.City]:
    cities:dict[str:bc.City] = {}
    folder = _file + "cities/"
    files = os.listdir(folder)
    print(files)

    for file in files:
        data = saves.Saves(folder + get_country_json_file(file))
        data.loaded_data[key] = val
        #data.loaded_data["location"]["y"] += 50
        del data.loaded_data["autonomy"]
        data.save()


    return cities

def a_add_to_cities(_file:str, key, val) -> dict[str:ba.Area]:
    areas: dict[str:ba.Area] = {}

    folder = _file + "areas/"
    files = os.listdir(folder)
    print(files)

    for file in files:
        data = saves.Saves(folder + get_country_json_file(file))
        cities = c_add_to_cities(folder + file + "/", data.loaded_data["name"] + "/", key, val)
        data.loaded_data[key] = val
        data.save()


    return areas

def add_to_cities(key, val) -> dict[str:country.Country]:
    returned_countries: dict[str:country.Country] = {}

    folder = "data/countries/"
    files = os.listdir(folder)
    print(files)
    for file in files:
        data = saves.Saves(folder + get_country_json_file(file)).loaded_data
        name = data["name"]
        areas = a_add_to_cities(folder + name + "/", key, val)

    return returned_countries
