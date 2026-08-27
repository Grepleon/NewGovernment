import politicians.policy.powers.military_authority as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class General(bjt.BaseJobTitle):
    name:str|None = "генерал"
    salary:int|None = 6_500
    power:bp.BasePower|None = p.MilitaryAuthority()
    importance = 8


