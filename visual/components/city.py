import visual.components.base_object as b_object
import visual.display
from countries.cities.base_city import City
from countries.areas.base_area import Area
from hints.lite import lite

class VisualObjectCity(b_object.BaseObject):
    def __init__(self, x1, y1, x2, y2,
                 city:City, area:Area,
                 tag, display: visual.display.Display, name="NULL"):
        super().__init__(tag, display)
        self.x1, self.y1, self.x2, self.y2 = x1, y1, x2, y2

        self.name = name

        self.city: City = city
        self.area: Area = area

        self.into_mouse=False
        self.on=False

        self._create()

    def disable(self):
        self.on=False


    def _create(self):
        self.display.create_circle(self.x1, self.y1, self.x2, self.y2,
                                      color=self.area.color, outline="black", tag=self.object_id)

    def display_object(self):
        if not self.on:
            if self.into_mouse:
                self.display.recolor(lite(self.area.color, 33), self.object_id)
            else:
                self.display.recolor(self.area.color, self.object_id)
        else:
            if self.into_mouse:
                self.display.recolor(lite(self.area.color, 33), self.object_id)
            else:
                self.display.recolor(self.area.color, self.object_id)

    def mouse_into_object(self, mx, my):
        self.into_mouse = self.x1 <= mx <= self.x2 and self.y1 <= my <= self.y2
        return self.into_mouse

    def mouse_clicked_object(self):
        self.on = self.into_mouse and not self.on
        return self.on

    def delete(self):
        self.display.delete(self.object_id)

    def hide(self):
        self.display.hide(self.object_id)

    def show(self):
        self.display.show(self.object_id)

