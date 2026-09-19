class Characteristic:
    name = None
    bio = None
    populism_level = 1.15

    def to_str(self):
        return self.name + ": " + self.bio

    def kill(self):
        return False

    def new_month(self):
        pass

    def tranquility(self, lvls:int):
        pass

    def anxiety(self, lvls:int):
        pass

    def start(self):
        pass

    def check_health(self) -> int:
        return 0

    def check_mind(self) -> int:
        return 0

    def get_populism(self) -> float:
        return self.populism_level