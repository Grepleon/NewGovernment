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

characters = []

def variable_characters() -> dict[str:pol.Politician]:
    # data = saves.Saves("data/characters/characters/politicians").loaded_data
    politicians: dict[str:pol.Politician] = {}

    folder = "data/characters/politicians/"
    # Конкретная папка
    files = os.listdir(folder)
    print(files)

    for file in files:
        data_pol = saves.Saves(folder + file).loaded_data
        #data_pol:dict = data[data_pol2]
        politicians[data_pol["name"]] = pol.Politician(
            data_pol["name"],
            data_pol["year"],
            pol_com.PoliticalCompass(data_pol["political_compass"]["left-right"],
                                     data_pol["political_compass"]["freedom"]),
            [str_to_ch.str_to_characteristic(val) for val in data_pol["characteristics"]],
            data_pol["money"],
            data_pol["alive"],
            data_pol["at_large"],
            str_to_pos.str_to_job_title(data_pol["position"]),
            pi.Popularity(
                data_pol["popularity"]["youth"],
                data_pol["popularity"]["middle-aged"],
                data_pol["popularity"]["elderly"],
                data_pol["popularity"]["in_power"],
                data_pol["popularity"]["poor"],
                data_pol["popularity"]["rich"]
            ),
            support.Support(
                data_pol["support"]["media"],
                data_pol["support"]["oligarchs"],
                data_pol["support"]["military"],
                data_pol["support"]["foreign"],
                data_pol["support"]["religious"],
            ),
            data_pol["mind"],
            data_pol["old_age"],
            data_pol["track"],
            data_pol["location"],
            data_pol["citizenship"],
            data_pol["place_of_residence"],
            data_pol["party"],
            data_pol["nickname"],
            data_pol["bio"]
        )

    return politicians

def get_country_json_file(val:str):
    return val + '/' + val + '.json'

def get_cities(_file:str, area:str) -> dict[str:bc.City]:
    cities:dict[str:bc.City] = {}
    folder = _file + "cities/"
    files = os.listdir(folder)
    print(files)

    for file in files:
        data = saves.Saves(folder + get_country_json_file(file)).loaded_data
        cities[data["name"]] = bc.City(
            data["name"],
            data["mayor"],
            Location(
                data["location"]["x"],
                data["location"]["y"]
            ),
            [buildings.Building(
                data["infrastructure"][data_build]["name"],
                data["infrastructure"][data_build]["type"],
                data["infrastructure"][data_build]["cost"],
                data["infrastructure"][data_build]["every_month_cost"]
            ) for data_build in data["infrastructure"]],
            data["population"],
            data["budget"]
        )


    return cities

def get_areas(_file:str) -> dict[str:ba.Area]:
    areas: dict[str:ba.Area] = {}

    folder = _file + "areas/"
    files = os.listdir(folder)
    print(files)

    for file in files:
        data:dict = saves.Saves(folder + get_country_json_file(file)).loaded_data
        cities = get_cities(folder + file + "/", data["name"] + "/")
        areas[data["name"]] = ba.Area(
            data["name"],
            cities,
            data["governor"],
            data["costs"],
            data["budget"],
            data["color"]
        )


    return areas

def variables_country() -> dict[str:country.Country]:
    returned_countries: dict[str:country.Country] = {}

    folder = "data/countries/"
    files = os.listdir(folder)
    print(files)
    for file in files:
        data = saves.Saves(folder + get_country_json_file(file)).loaded_data
        name = data["name"]
        areas = get_areas(folder + name + "/")
        returned_countries[name] = country.Country(
            name,
            data["name_capital"],
            data["officials"]["president"],
            areas,
            data["officials"]["ministry_of_finance"],
            data["officials"]["ministry_of_internal_affairs"],
            data["officials"]["ministry_of_foreign_affairs"],
            data["officials"]["ministry_of_defence"],
            data["officials"]["ministry_of_social_policy"],
            data["officials"]["ministry_of_justice"],
            data["officials"]["prime_minister"],
            data["officials"]["head_of_cb"],
            data["budget"],
            data["costs"],
            data["color"]
        )

    return returned_countries

if __name__ == "__main__":
    pols = variable_characters()

    for pol2 in pols:
        print(pol2.to_str())