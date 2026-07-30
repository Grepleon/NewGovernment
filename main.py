import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button
import visual.managers.manager as manager
import visual.managers.all_menu as path_all_menu

def create_politicians() -> dict[str:path_politician.Politician]:
    _politicians = variable_characters()

    for politician in _politicians:
        data_politician = _politicians[politician]
        data_politician.start()

    return _politicians

politicians = create_politicians()

display = visual.mainloop.Display(config.width, config.height)
all_menu = path_all_menu.AllMenu(display, politicians)

all_menu.checker()

display.end()
