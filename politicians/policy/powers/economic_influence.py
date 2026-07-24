import politicians.policy.powers.base_power as base_power

class EconomicInfluence(base_power.BasePower):
    name = "экономическое влияние"

    def event(self):
        """выделить деньги на исполнение закона"""

    def initiative(self):
        """выделить деньги на инвестиции/субсидии"""
