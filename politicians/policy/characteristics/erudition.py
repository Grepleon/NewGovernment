import politicians.policy.characteristics.characteristic as ch

class Erudition(ch.Characteristic):
    name = "Эрудиция"
    bio = "является умным и начитанным"


    def check_mind(self) -> int:
        return 10