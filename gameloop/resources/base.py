class Resources:
    name = None
    def __init__(self, explored_quantity, unexplored_quantity,
                 extracted, quality, local_quality):
        self.explored_quantity = explored_quantity
        self.unexplored_quantity = unexplored_quantity
        self.extracted = extracted
        self.quality = quality
        self.local_quality = local_quality

    def to_str(self) -> str:
        return (f"{self.name}:\n"
                f"- разработано: {self.explored_quantity} ед., {round(self.quality * 100, 1)}%"
                f"\n- добыто: {self.extracted} ед., {round(self.local_quality * 100, 1)}%"
                )