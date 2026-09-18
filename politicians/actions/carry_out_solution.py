from politicians.actions.solutions import make_a_declaration

dict_solutions = {
    "провести большое интервью": make_a_declaration.carry_out
}

def carry_out_solutions(name_sol, display, game_states, politician):
    print(name_sol)
    if name_sol in dict_solutions:
        print('x')
        dict_solutions[name_sol](politician, display, game_states)
