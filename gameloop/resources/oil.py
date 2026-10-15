from gameloop.resources.base import Resources

class Oil(Resources):
    def __init__(self, explored_quantity, unexplored_quantity,
                 extracted, quality, local_quality):
        super().__init__(explored_quantity, unexplored_quantity,
                 extracted, quality, local_quality)
        self.name = "Нефть"
