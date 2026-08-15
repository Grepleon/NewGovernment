import politicians.nation.base_nation as bn
import hints.int_to_str as its

class EthnicGroup:
    def __init__(self, nation:str, count:int):
        self.nation:str = nation
        self.count:int = count

    def to_str(self):
        return f"{self.nation}: {its.int_to_str(int(self.count * 100))}%"