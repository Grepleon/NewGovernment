from politicians.actions.solutions import make_a_declaration
from politicians.actions.solutions import to_deliver_a_speech
from politicians.actions.solutions import provocative_statement
from politicians.actions.solutions import conduct_a_major_interview
from politicians.actions.solutions import answer_off_the_cuff
from politicians.actions.solutions import youth_event

dict_solutions = {
    "сделать заявление": make_a_declaration.carry_out,
    "выступить с речью": to_deliver_a_speech.carry_out,
    "провокационное заявление": provocative_statement.carry_out,
    "провести большое интервью": conduct_a_major_interview.carry_out,
    "ответить без подготовки": answer_off_the_cuff.carry_out,
    "молодежная акция": youth_event.carry_out,
}

def carry_out_solutions(name_sol, display, game_states, politician):
    if name_sol in dict_solutions:
        dict_solutions[name_sol](politician, display, game_states)
    game_states.statistics.solutions[name_sol] = game_states.statistics.solutions.get(name_sol, 0) + 1
    game_states.statistics.counts += 1
