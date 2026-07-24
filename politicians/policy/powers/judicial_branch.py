import politicians.policy.powers.base_power as base_power

class JudicialBranch(base_power.BasePower):
    name = "судебная власть"

    def event(self):
        """рассмотреть закон (принять или отправить на доработку)"""

    def initiative(self):
        """судить в высшем суде"""
