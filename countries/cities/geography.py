class Geography:
    def __init__(self, height, forests, average_temperature, purity):
        self.height = height
        self.forests = forests
        self.average_temperature = average_temperature
        self.purity = purity

    def to_str(self):
        return f"{self.height}м, {'+' if self.average_temperature > 0 else ''}{self.average_temperature}°C"