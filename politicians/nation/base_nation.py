class Nation:
    def __init__(self, name:str, carrier:str):
        self.name = name
        self.carrier = carrier

    def to_str(self):
        return self.name