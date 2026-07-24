import politicians.policy.powers.base_power as base_power

class MilitaryAuthority(base_power.BasePower):
    name = "военная власть"

    def event(self):
        """организовать командование армией в военном столкновении"""

    def initiative(self):
        """отдать приказ армии"""
