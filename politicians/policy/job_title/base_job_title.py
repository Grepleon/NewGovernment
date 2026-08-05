import politicians.policy.powers.base_power as bp

class BaseJobTitle:
    name:str|None = None
    salary:int|None = None
    power:bp.BasePower|None = None

    def __init__(self):
        self.fines: list[int] = []

    def get_money(self) -> int:
        return self.salary - sum([fine for fine in self.fines])