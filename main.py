import os
import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters

def create_politicians() -> dict[str:path_politician.Politician]:
    politicians = variable_characters()

    for politician in politicians:
        data_politician = politicians[politician]
        data_politician.start()

    return politicians

display = visual.mainloop.Display(config.width, config.height)



display.end()
