from saves import Saves
from time import time as timer

class Statistics:
    def __init__(self, time):
        self.time = time
        self.time_start = timer()

def get_statistics():
    data = Saves("data/statistics/times.json").loaded_data
    statistics = Statistics(data["time"])

    return statistics

def set_statistics(statistics:Statistics):
    file = Saves("data/statistics/times.json")
    file.save_file({"time": statistics.time})