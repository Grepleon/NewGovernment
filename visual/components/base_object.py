import visual.mainloop as visual

class BaseObject:
    def __init__(self, tag, display: visual.Display):
        self.object_id:int|str = tag
        self.display = display

    def display_object(self):
        pass

    def delete(self):
        self.display.delete(self.object_id)

    def mouse_into_object(self, mx, my):
        pass

    def mouse_clicked_object(self):
        pass

    def hide(self):
        pass

    def show(self):
        pass