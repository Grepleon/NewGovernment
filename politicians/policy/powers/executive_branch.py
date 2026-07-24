import politicians.policy.powers.base_power as base_power

class ExecutiveBranch(base_power.BasePower):
    name = "исполнительная власть"

    def event(self):
        """организовать исполнение закона"""

    def initiative(self):
        """издать указ"""
