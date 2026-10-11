from gameloop.resources.base import Resources

class Electricity(Resources):
    def __init__(self, extracted):
        super().__init__(0, 0, extracted, 1, 1)
        self.name = "Электричество"
