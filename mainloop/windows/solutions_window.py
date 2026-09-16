from visual.components.base_object import BaseObject as GameObject
from mainloop.windows.additional_windows import AdditionalWindow
from visual.components.hint import Hint
from visual.display import Display
from visual.components.base_object import BaseObject
from visual.components.button import Button

def space(text:str, max_char:int, extra_max:int):
    count_char=0
    new_text = ""
    for char in text:
        count_char += 1
        if char == "\n":
            count_char = 0

        if char != " ":
            if count_char < extra_max:
                new_text += char
            else:
                new_text += char + "-\n"
                count_char = 0
        elif count_char > max_char:
            new_text += "\n"
            count_char = 0
        else:
            new_text += " "

    if new_text[-1] == "\n":
        new_text = new_text[:-1]
    if new_text[-1] == "-":
        new_text = new_text[:-1]

    return new_text.replace("-\n ", "\n")

class SolutionWindow(AdditionalWindow):
    hint:Hint|None = None

    def process(self):
        self.display.switch_window(self.name_window)
        if self.check_activity():
            self.hint.hide()

            for component in self.components:
                if type(component) == Button:
                    component:Button = component
                    if component.into_mouse:
                        self.hint.show()
                        self.hint.rewrite_text(space(component.name, 20, 25))
                        self.hint.to_move(
                            self.display.mouse_x,
                            self.display.mouse_y
                        )

        self.display.switch_window(self.display.main_window)