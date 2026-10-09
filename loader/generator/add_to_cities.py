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
        data.loaded_data["geography"]["resources"] = {
            "oil": {
                "explored": {
                    "quantity": 500,
                    "quality": 0.85
                },
                "unexplored": {
                    "quantity": 1200,
                    "quality": 0.85
                },
                "extracted": {
                    "quantity": 100,
                    "quality": 0.85
                }
            },
            "natural_gas": {
                "explored": {
                    "quantity": 3000,
                    "quality": 1
                },
                "unexplored": {
                    "quantity": 8000,
                    "quality": 1
                },
                "extracted": {
                    "quantity": 500,
                    "quality": 1
                }
            },
            "coal": {
                "explored": {
                    "quantity": 1000,
                    "quality": 0.6,
                    "open-pit_extraction": 0.5
                },
                "unexplored": {
                    "quantity": 8500,
                    "quality": 0.6,
                    "open-pit_extraction": 0.5
                },
                "extracted": {
                    "quantity": 4500,
                    "quality": 1
                }
            },
            "iron": {
                "explored": {
                    "quantity": 2000,
                    "quality": 0.5,
                    "open-pit_extraction": 0.95
                },
                "unexplored": {
                    "quantity": 3000,
                    "quality": 0.5,
                    "open-pit_extraction": 0.95
                },
                "extracted": {
                    "quantity": 250,
                    "quality": 0.5
                }
            },
            "non-ferrous_metals": {
                "explored": {
                    "quantity": 100,
                    "quality": 0.25,
                    "open-pit_extraction": 1
                },
                "unexplored": {
                    "quantity": 250,
                    "quality": 0.25,
                    "open-pit_extraction": 1
                },
                "extracted": {
                    "quantity": 10,
                    "quality": 0.25
                }
            },
            "rare_earths": {
                "explored": {
                    "quantity": 3500,
                    "quality": 0.6,
                    "open-pit_extraction": 1
                },
                "unexplored": {
                    "quantity": 10000,
                    "quality": 0.6,
                    "open-pit_extraction": 1
                },
                "extracted": {
                    "quantity": 500,
                    "quality": 0.6
                }
            },
            "uranium": {
                "explored": {
                    "quantity": 250,
                    "quality": 0.5,
                    "open-pit_extraction": 0.8
                },
                "unexplored": {
                    "quantity": 250,
                    "quality": 0.5,
                    "open-pit_extraction": 0.8
                },
                "extracted": {
                    "quantity": 10,
                    "quality": 0.5
                }
            },
            "gold": {
                "explored": {
                    "quantity": 500,
                    "quality": 0.2,
                    "open-pit_extraction": 0.95
                },
                "unexplored": {
                    "quantity": 3000,
                    "quality": 0.2,
                    "open-pit_extraction": 0.95
                },
                "extracted": {
                    "quantity": 10,
                    "quality": 0.2
                }
            },
            "gems": {
                "explored": {
                    "quantity": 125,
                    "quality": 0.2,
                    "open-pit_extraction": 0.95
                },
                "unexplored": {
                    "quantity": 1200,
                    "quality": 0.2,
                    "open-pit_extraction": 0.95
                },
                "extracted": {
                    "quantity": 20,
                    "quality": 0.2
                }
            },
            "wood": {
                "explored": {
                    "quantity": 50000,
                },
                "extracted": {
                    "quantity": 10000,
                }
            },
            "electricity": {
                "extracted": {
                    "quantity": 2500,
                }
            },
        }
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
