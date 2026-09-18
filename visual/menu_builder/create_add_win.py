import config
from config import solutions
from mainloop.game_states import GameState
from mainloop.windows.solutions_window import SolutionWindow
from mainloop.windows.additional_windows import AdditionalWindow
from saves import Saves
from visual.components.button import Button
from visual.components.hint import Hint
from hints.enters import space

def create_add_win(game_state:GameState, win_name:str, add_win:SolutionWindow):
    display = game_state.display
    display.switch_window(win_name)

    folder = r"data/solutions/"
    file = win_name.replace(" ", "") + ".json"
    solution = Saves(folder + file).loaded_data
    display.create_text(
        config.size_add_win_x / 2, 15,
        solution["name"].upper(),
        config.base_on_button_color
    )

    out_x = 10
    out_y = 55
    out_y2 = 5

    size_button_y = 35
    gap_x = 5
    gap_y = 25

    for index_y, data_solution in enumerate(solution["solutions"]):
        into_solution = solution["solutions"][data_solution]

        count = len(into_solution)

        # Ширина, которую вообще можно использовать
        available_width = config.size_add_win_x - out_x * 2

        # Вычитаем промежутки между кнопками
        buttons_width = available_width - gap_x * (count - 1)

        # Ширина одной кнопки
        size_button_x = buttons_width / count

        display.create_text(config.size_add_win_x / 2,
                            out_y + index_y * (size_button_y + gap_y) - gap_y / 2,
                            data_solution, config.add_text_color)

        for index_x, name_into_solution in enumerate(into_solution):
            x1 = out_x + index_x * (size_button_x + gap_x)
            x2 = x1 + size_button_x

            y1 = out_y + index_y * (size_button_y + gap_y)
            y2 = y1 + size_button_y
            button = Button(
                    x1,
                    y1,
                    x2,
                    y2,

                    config.base_off_button_color,
                    config.base_off_bg_button_color,
                    config.base_on_button_color,
                    config.base_on_bg_button_color,

                    space(name_into_solution, abs(x2 - x1) // 10, abs(x2 - x1) // 8),

                    display.add_id(),
                    display,
                    game_state,
                    into_solution[name_into_solution]["hint"]
            )
            button.add_info("polh", into_solution[name_into_solution]["cost"])
            button.add_info("name", name_into_solution)

            add_win.components.append(
                button
            )
    add_win.components.append(
        Button(
            out_x,
            config.size_add_win_y - out_y2,
            config.size_add_win_x - out_x,
            config.size_add_win_y - size_button_y - out_y2,

                    config.cancel_off_button_color,
                    config.cancel_off_bg_button_color,
                    config.cancel_on_button_color,
                    config.cancel_on_bg_button_color,

                    "Подтвердить",

                    display.add_id(),
                    display
        )
    )
    add_win.last_button = add_win.components[-1]
    hint:Hint = Hint(
            5, 5,

            config.base_off_button_color,
            config.base_off_bg_button_color,

            "Информационное поле",

            display.add_id(),
            display
        )
    add_win.components.append(
        hint
    )
    add_win.hint = hint
    hint.width = config.size_add_win_x
    hint.height = config.size_add_win_y

    display.switch_window(display.main_window)
