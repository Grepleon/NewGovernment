from politicians.actions.solutions import make_a_declaration

dict_solutions = {
    "провести большое интервью": make_a_declaration.carry_out
}

def carry_out_solutions(name_sol, display, game_states, politician):
    if name_sol in dict_solutions:
        dict_solutions[name_sol](politician, display, game_states)
    game_states.statistics.solutions[name_sol] = game_states.statistics.solutions.get(name_sol, 0) + 1
    game_states.statistics.counts += 1
