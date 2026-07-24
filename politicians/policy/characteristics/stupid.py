import politicians.policy.characteristics.characteristic as ch

class Stupid(ch.Characteristic):
    name = "Глупость"
    bio = "более глупый человек худшим образом делает или отвечает"

    def check_mind(self) -> int:
        return -20