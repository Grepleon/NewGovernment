import politicians.policy.powers.economic_influence as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class HeadCB(bjt.BaseJobTitle):
    name:str|None = "глава ЦБ"
    salary:int|None = 8_000
    power:bp.BasePower|None = p.EconomicInfluence()
    importance = 8
