from mainloop.game_states import GameState
from hints.int_to_str import int_to_str as its

class Var:
    def __init__(self, name, value):
        self.name = name
        self.value = value

class Code:
    def __init__(self, list_code, game_state:GameState):
        self.vars:dict[str:Var] = {}
        self.code:list[list[str]] = list_code
        self.game_state = game_state

    def define(self, word):
        if word == "PRINT":
            return word, 1
        else:
            return None, 0

    def execute(self):
        for line in self.code:
            actions = None
            len_action = 0
            for word in line:
                if actions is None:
                    actions, len_action = self.define(word)
                else:
                    len_action -= 1
                    if actions == "PRINT":
                        print(word.replace("\"", ""))
                    if len_action == 0:
                        actions = None


def parser(code):
    list_code = code.split("\n")
    lists = []
    for line in list_code:
        words = []
        word = ""
        is_str = False
        for char in line:
            if not is_str:
                if char == "\"":
                    is_str = True
                if char != " ":
                    word += char
                else:
                    words.append(word)
                    word = ""
            else:
                word += char
                if char == "\"":
                    word += char
        words.append(word)

        lists.append(words)
    return lists

def execute(str_code:str, game_state:GameState):
    list_code = parser(str_code)
    code = Code(list_code, game_state)
    code.execute()
    print(list_code)

"""
NUM random <RANDOM:2,5>
ADD <POP->PEOPLES> random
"""