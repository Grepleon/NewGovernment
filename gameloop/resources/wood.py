from gameloop.resources.base import Resources

class Wood(Resources):
    def __init__(self, explored_quantity, extracted, quality, local_quality):
        super().__init__(explored_quantity, 0,
                 extracted, quality, local_quality)
        self.name = "Дерево"