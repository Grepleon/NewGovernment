from gameloop.resources.base import Resources

class Wood(Resources):
    name = "Дерево"

    def __init__(self, explored_quantity, extracted, quality, local_quality):
        super().__init__(explored_quantity, 0,
                 extracted, quality, local_quality)
