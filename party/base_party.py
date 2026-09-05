import politicians.politician as pol
import politicians.policy.political_compass as pol_com

class BaseParty:
    def __init__(self, name, leader: pol.Politician, participants: list[pol.Politician],
                 political_ideas:pol_com.PoliticalCompass):
        self.name:str = name
        self.leader: pol.Politician = leader
        self.participants: list[pol.Politician] = participants
        self.political_ideas = political_ideas