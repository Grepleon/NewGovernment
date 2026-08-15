from saves import Saves
from time import time as timer

class Statistics:
    def __init__(self, time, count_politicians: dict[str:int]):
        self.time = time
        self.time_start = timer()
        self.count_politicians = count_politicians

    def add_selected_politician(self, politician):
        print(self.count_politicians)
        self.count_politicians[politician] = self.count_politicians.get(politician, 0) + 1

def get_statistics():
    data_time = Saves("data/statistics/times.json").loaded_data
    data_counts = Saves("data/statistics/counts.json").loaded_data

    statistics = Statistics(data_time["time"], data_counts["selected_politician"])

    return statistics

def set_statistics(statistics:Statistics):
    file = Saves("data/statistics/times.json")
    file.save_file({
        "time": statistics.time
    })

    file = Saves("data/statistics/counts.json")
    file.save_file({
        "selected_politician": statistics.count_politicians
    })