import politicians.policy.characteristics.characteristic as ch

class PoorHealth(ch.Characteristic):
    name = "Плохое здоровье"
    bio = "раньше начинает стареть"

    def check_health(self) -> int:
        return -15