import config
import visual.components.base_object as b_object
import visual.display

class Hint(b_object.BaseObject):
    def __init__(self, x, y,
                 color, bg_color,  text, tag, display: visual.display.Display, name="NULL"):
        super().__init__(tag, display)
        self.name = name
        self.color = color
        self.bg_color = bg_color
        self.x, self.y = x, y
        self.text = text
        self.pref_text = "-TEXT"
        self._create()
        self.out_x = 5
        self.out_y = 0

    def size_to_text(self, x=6, y=17) -> tuple[int, int]:
        val = self.text
        return x * len(max(val.split("\n"), key=lambda x: len(x))), len(val.split("\n")) * y

    def hide(self):
        self.display.hide(self.object_id)
        self.display.hide(self.object_id + self.pref_text)

    def show(self):
        self.display.show(self.object_id)
        self.display.show(self.object_id + self.pref_text)

    def delete(self):
        self.display.delete(self.object_id)
        self.display.delete(self.object_id + self.pref_text)

    def _create(self):
        dx, dy = self.size_to_text()
        if self.x + dx > config.width:
            dx *= -1
        if self.y + dy > config.height:
            dy *= -1

        self.display.create_rectangle(self.x, self.y, self.x + dx, self.y + dy,
                                      color=self.bg_color, outline=self.color,
                                      tag=self.object_id)
        self.display.create_text((self.x + self.x + dx) / 2, (self.y + self.y + dy) / 2,
                                 text=self.text, tag=self.object_id+self.pref_text, color=self.color)

    def to_move(self, new_x, new_y):
        self.x = new_x
        self.y = new_y

    def recolor(self, color, bg_color):
        self.color = color
        self.bg_color = bg_color

        self.display.recolor(bg_color, self.object_id)
        self.display.recolor_outline(color, self.object_id)
        self.display.recolor(color, self.object_id + self.pref_text)

    def rewrite_text(self, new_text):
        self.text = new_text

    def display_this(self, x=6, y=17):
        dx, dy = self.size_to_text(x, y)
        out_x = self.out_x
        out_y = self.out_y
        if self.x + dx + self.out_x > config.width:
            dx *= -1
            out_x *= -1
        if self.y + dy + self.out_y> config.height:
            dy *= -1
            out_y *= -1

        if self.y + dy + out_y > config.height or out_y + dy + self.y < 0:
            self.y = 5
            dy *= -1
            out_y *= -1

        self.display.rewrite_text(self.text, self.object_id + self.pref_text)
        self.display.move_to_coord(self.object_id, self.x + out_x, self.y + out_y,
                                   self.x + dx + out_x, self.y + dy + out_y)
        self.display.move_to_coord2(self.object_id + self.pref_text,
               (self.x * 2 + out_x * 2 + dx) / 2, (self.y * 2 + out_y * 2 + dy) / 2)

    def display_object(self, x1=6, y1=17):
        self.display_this(x=x1, y=y1)