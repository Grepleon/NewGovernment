import saves
import os
import politicians.politician as pol, politicians.policy.political_compass as pol_com
import politicians.policy.str_to_characteristic as str_to_ch
import politicians.policy.str_to_job_title as str_to_pos
import politicians.policy.popularity.popularity_indicator as pi
import politicians.policy.popularity.support as support

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
                data_pol["popularity"]["reach"]
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

if __name__ == "__main__":
    pols = variable_characters()

    for pol2 in pols:
        print(pol2.to_str())