import politicians.policy.powers.base_power as base_power

class LegislativeBranch(base_power.BasePower):
    name = "законодательная власть"

    def event(self):
        """голосование за закон"""

    def initiative(self):
        """продвинуть какой-либо закон"""
