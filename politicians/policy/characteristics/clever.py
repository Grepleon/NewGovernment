import politicians.policy.characteristics.characteristic as ch

class Clever(ch.Characteristic):
    name = "Ум"
    bio = "более умный человек лучшим образом делает или отвечает"

    def check_mind(self) -> int:
        return 15