class Resources:
    def __init__(self, name, explored_quantity, unexplored_quantity,
                 extracted, quality, local_quality):
        self.name = name
        self.explored_quantity = explored_quantity
        self.unexplored_quantity = unexplored_quantity
        self.extracted = extracted
        self.quality = quality
        self.local_quality = local_quality

    def get_res(self) -> str:
        return (f"{self.name}:\n"
                f"изучено: {self.explored_quantity} ед., {round(self.quality * 100, 1)}%"
                f"добыто: {self.extracted} ед., {round(self.local_quality * 100, 1)}%"
                )