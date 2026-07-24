import politicians.politician as pol

class BaseParty:
    def __init__(self, name, leader: pol.Politician, participants: list[pol.Politician]):
        self.name:str = name
        self.leader: pol.Politician = leader
        self.participants: list[pol.Politician] = participants