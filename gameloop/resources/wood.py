from gameloop.resources.base import Resources

class Wood(Resources):
    def __init__(self, explored_quantity, extracted):
        super().__init__(explored_quantity, 0,
                 extracted,1, 1)
        self.name = "Дерево"