from saves import Saves
from time import time as timer

class Statistics:
    def __init__(self,
                 time,
                 count_politicians: dict[str:int],
                 launches,
                 maps_choose,
                 max_game_time,
                 game_time,
                 max_date_time
                 ):
        self.time = time
        self.time_start = timer()
        self.count_politicians = count_politicians
        self.launches = launches
        self.maps_choose = maps_choose
        self.max_game_time = max_game_time
        self.game_time = game_time
        self.max_date_time = max_date_time

    def add_selected_politician(self, politician):
        self.count_politicians[politician] = self.count_politicians.get(politician, 0) + 1

def get_statistics():
    data_time = Saves("data/statistics/times.json").loaded_data
    data_counts = Saves("data/statistics/counts.json").loaded_data
    data_play_time = Saves("data/statistics/play_time.json").loaded_data

    statistics = Statistics(data_time["time"],
                            data_counts["selected_politician"],
                            data_counts["launches"] + 1,
                            data_counts["maps_choose"],
                            data_play_time["max_time"],
                            data_play_time["time"],
                            data_play_time["max_date"])

    return statistics

def set_statistics(statistics:Statistics):
    file = Saves("data/statistics/times.json")
    file.save_file({
        "time": statistics.time
    })

    file = Saves("data/statistics/counts.json")
    file.save_file({
        "selected_politician": statistics.count_politicians,
        "launches": statistics.launches,
        "maps_choose": statistics.maps_choose
    })

    file = Saves("data/statistics/play_time.json")
    file.save_file({
        "max_time": statistics.max_game_time,
        "max_date": statistics.max_date_time,
        "time": statistics.game_time
    })