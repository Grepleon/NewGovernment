import os
import config
import politicians.politician as path_politician
import visual.mainloop
from politicians.characters.variables import variable_characters
import visual.components.button as button

def create_politicians() -> dict[str:path_politician.Politician]:
    politicians = variable_characters()

    for politician in politicians:
        data_politician = politicians[politician]
        data_politician.start()

    return politicians

display = visual.mainloop.Display(config.width, config.height)

main_button_coordinates = config.main_button_coordinates
main_button = button.Button(config.main_button_coordinates[0], config.main_button_coordinates[1],
                    config.main_button_coordinates[2], config.main_button_coordinates[3],
                    config.base_off_button_color, config.base_off_bg_button_color,
                    config.base_on_button_color, config.base_on_bg_button_color,
                    config.main_button_text, display.add_id(), display)
main_button.display_object()

display.end()
