import os
import config
import politicians.politician as path_politician
import visual.display
from politicians.characters.variables import variable_characters
import visual.components.button as button

def create_politicians() -> dict[str:path_politician.Politician]:
    politicians = variable_characters()

    for politician in politicians:
        data_politician = politicians[politician]
        data_politician.start()

    return politicians

display = visual.mainloop.Display(config.width, config.height)

test_button = button.Button(100, 200, 500, 400, "#00ff00", "#003300",
                "#33ff33", "#228822", "Тест-кнопка", display.add_id(), display)
test_button.display_object()

display.end()