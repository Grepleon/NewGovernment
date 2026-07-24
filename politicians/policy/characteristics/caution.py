import politicians.policy.characteristics.characteristic as ch

class Caution(ch.Characteristic):
    name = "Осторожность"
    bio = "предпочтет перепроверить, прежде чем ответит, реже ошибается"

    def check_mind(self) -> int:
        return 10