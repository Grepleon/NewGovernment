import politicians.policy.characteristics.characteristic as ch

class GoodHealth(ch.Characteristic):
    name = "Хорошее здоровье"
    bio = "позже начинает стареть"

    def check_health(self) -> int:
        return 10