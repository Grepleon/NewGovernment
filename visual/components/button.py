import visual.components.base_object as b_object
import visual.mainloop


class Button(b_object.BaseObject):
    def __init__(self, x1, y1, x2, y2,
                 color, bg_color, active_color, bg_active_color,
                 text, tag, display: visual.mainloop.Display):
        super().__init__(tag, display)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2
        self.color, self.bg_color, self.active_color, self.bg_active_color =\
            color, bg_color, active_color, bg_active_color
        self.text = text
        self.pref_text = "-T"

        self.into_mouse=False
        self.on=False

        self._create()

    def _create(self):
        self.display.create_rectangle(self.x1, self.y1, self.x2, self.y2,
                                      color=self.bg_color, outline=self.color, tag=self.object_id)
        self.display.create_text(self.x1 / 2 + self.x2 / 2, self.y1 / 2 + self.y2 / 2,
                                 self.text, self.color, tag=self.object_id + self.pref_text)

    def display_object(self):
        if not self.on:
            if self.into_mouse:
                self.display.recolor(self.color, self.object_id)
                self.display.recolor(self.bg_color, self.object_id + self.pref_text)
            else:
                self.display.recolor(self.bg_color, self.object_id)
                self.display.recolor(self.color, self.object_id + self.pref_text)
        else:
            if self.into_mouse:
                self.display.recolor(self.active_color, self.object_id)
                self.display.recolor(self.bg_active_color, self.object_id + self.pref_text)
            else:
                self.display.recolor(self.bg_active_color, self.object_id)
                self.display.recolor(self.active_color, self.object_id + self.pref_text)

    def mouse_into_object(self, mx, my):
        self.into_mouse = self.x1 <= mx <= self.x2 and self.y1 <= my <= self.y2
        return self.into_mouse

    def mouse_clicked_object(self):
        self.on = self.into_mouse and not self.on
        return self.on

    def delete(self):
        self.display.delete(self.object_id)
        self.display.delete(self.object_id + self.pref_text)