from random import randint, choice
import visual.components.base_object as bo
import config

class Noice(bo.BaseObject):
    quantity = config.quantity_noice
    colors = config.colors_noice
    size = config.size_noice
    pref = ':i'

    def __init__(self, tag, display):
        super().__init__(tag, display)
        self.create()
        self.pref = ':i'

    def create(self):
        for index in range(self.quantity):
            color = choice(self.colors)
            x = randint(0, config.width)
            y = randint(0, config.height)

            self.display.create_rectangle(x, y, x + self.size, y + self.size,
                                          color, color, self.object_id + self.pref + str(index))
            self.display.recolor(color, self.object_id + self.pref + str(index))


    def display_object(self):
        for index in range(self.quantity):
            x = randint(0, config.width)
            y = randint(0, config.height)

            color = choice(self.colors)

            self.display.move_to_coord(self.object_id + self.pref + str(index), x, y, x + self.size * 5, y + self.size)
            self.display.recolor(color, self.object_id + self.pref + str(index))

    def hide(self):
        for index in range(self.quantity):
            self.display.hide(self.object_id + self.pref + str(index))

    def show(self):
        for index in range(self.quantity):
            self.display.show(self.object_id + self.pref + str(index))

