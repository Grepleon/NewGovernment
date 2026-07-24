import politicians.policy.characteristics.characteristic as ch

class Lawyer(ch.Characteristic):
    name = "Юрист"
    bio = "легче находить лазейки, взяточничество и правонарушения"

    def check_mind(self) -> int:
        return 5