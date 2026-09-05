import politicians.politician as pol
import politicians.policy.political_compass as pol_com

class BaseParty:
    def __init__(self, name, leader: str, participants: list[str],
                 political_ideas:pol_com.PoliticalCompass):
        self.name:str = name
        self.leader: str = leader
        self.participants: list[str] = participants
        self.political_ideas:pol_com.PoliticalCompass = political_ideas