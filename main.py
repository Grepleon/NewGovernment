import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button
import visual.managers.manager as manager
import visual.managers.all_menu as path_all_menu

def create_politicians() -> dict[str:path_politician.Politician]:
    politicians = variable_characters()

    for politician in politicians:
        data_politician = politicians[politician]
        data_politician.start()

    return politicians


display = visual.mainloop.Display(config.width, config.height)
all_menu = path_all_menu.AllMenu(display)

all_menu.checker()

display.end()
