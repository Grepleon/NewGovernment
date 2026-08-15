import politicians.nation.base_nation as bn
import hints.int_to_str as its

class EthnicGroup:
    def __init__(self, nation:bn.Nation, count:int):
        self.nation:bn.Nation = nation
        self.count:int = count

    def to_str(self):
        return f"{self.nation.to_str()}: {its.int_to_str(self.count)}"