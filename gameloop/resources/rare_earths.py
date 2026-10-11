from gameloop.resources.base import Resources

class RareEarths(Resources):
    name = "Редкоземельные металлы"

    def __init__(self, explored_quantity, unexplored_quantity,
                 extracted, quality, local_quality, open_pit_extraction):
        super().__init__(explored_quantity, unexplored_quantity,
                 extracted, quality, local_quality)
        self.open_pit_extraction = open_pit_extraction