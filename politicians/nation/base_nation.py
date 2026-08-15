class Nation:
    def __init__(self, name:str, carrier:str, color:str="#ffffff"):
        self.name = name
        self.carrier = carrier
        self.color = color

    def to_str(self):
        return self.name