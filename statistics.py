from saves import Saves
from time import time as timer
import shutil, os

class Statistics:
    def __init__(self,
                 time,
                 count_politicians: dict[str:int],
                 launches,
                 maps_choose,
                 max_game_time,
                 game_time,
                 max_date_time,
                 winners,
                 votes,
                 yours_win,
                 max_points,
                 quantity_events,
                 selected_actions,
                 events
                 ):
        self.time = time
        self.time_start = timer()
        self.count_politicians = count_politicians
        self.launches = launches
        self.maps_choose = maps_choose
        self.max_game_time = max_game_time
        self.game_time = game_time
        self.max_date_time = max_date_time
        self.winners = winners
        self.yours_win = yours_win
        self.votes = votes
        self.max_points = max_points
        self.quantity_events = quantity_events
        self.selected_actions = selected_actions
        self.events = events

    def add_selected_politician(self, politician):
        self.count_politicians[politician] = self.count_politicians.get(politician, 0) + 1

    def check_votes(self, job, winner, points, you="NULL"):
        if job not in self.winners:
            self.winners[job] = {}
        if job not in self.yours_win:
            self.yours_win[job] = {}
        self.winners[job][winner] = self.winners[job].get(winner, 0) + 1
        self.max_points[job] = max(self.max_points[job], points)
        self.votes += 1
        if you == winner:
            self.yours_win[job][winner] = self.yours_win[job].get(winner, 0) + 1

    def check_events(self, selected_event, event_name):
        self.quantity_events += 1
        self.selected_actions[selected_event] = self.selected_actions.get(selected_event, 0) + 1
        self.events[event_name] = self.events.get(event_name, 0) + 1

def check_first():
    destination = r"data/statistics/"
    source = r"data/statistics_recording/"
    if not os.path.exists(destination):
        shutil.copytree(source, destination)
        print("Папка успешно скопирована")

def get_statistics():
    check_first()

    data_time = Saves("data/statistics/times.json").loaded_data
    data_counts = Saves("data/statistics/counts.json").loaded_data
    data_play_time = Saves("data/statistics/play_time.json").loaded_data
    data_vote = Saves("data/statistics/votes.json").loaded_data
    data_events = Saves("data/statistics/actions.json").loaded_data

    statistics = Statistics(data_time["time"],
                            data_counts["selected_politician"],
                            data_counts["launches"] + 1,
                            data_counts["maps_choose"],
                            data_play_time["max_time"],
                            data_play_time["time"],
                            data_play_time["max_date"],
                            data_vote["winners"],
                            data_vote["votes"],
                            data_vote["yours_win"],
                            data_vote["max_points"],
                            data_events["quantity_events"],
                            data_events["selected_actions"],
                            data_events["events"]
                            )

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

    file = Saves("data/statistics/votes.json")
    file.save_file({
        "winners": statistics.winners,
        "votes": statistics.votes,
        "max_points": statistics.max_points,
        "yours_win": statistics.yours_win
    })

    file = Saves("data/statistics/actions.json")
    file.save_file({
        "quantity_events": statistics.quantity_events,
        "selected_actions": statistics.selected_actions,
        "events": statistics.events
    })

def save(statistics:Statistics, game_state):
    statistics.time += timer() - statistics.time_start
    statistics.game_time += game_state.ticks

    if statistics.max_game_time < game_state.ticks:
        statistics.max_game_time = game_state.ticks
        statistics.max_date_time = game_state.get_str_year()