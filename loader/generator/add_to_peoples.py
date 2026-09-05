import os, saves

def variable_characters():
    # data = saves.Saves("data/characters/characters/politicians").loaded_data
    politicians = {}

    folder = "data/characters/politicians/"
    # Конкретная папка
    files = os.listdir(folder)
    print(files)

    for file in files:
        data = saves.Saves(folder + file)
        data.loaded_data["participating"] = {"ruler":False, "governor":False, "mayor":False, "deputy":False}
        data.loaded_data["blocked"] = {"ruler":False, "governor":False, "mayor":False, "deputy":False}
        print(file)
        data.save()
