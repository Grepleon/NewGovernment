import politicians.policy.powers as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Unemployed(bjt.BaseJobTitle):
    name:str|None = "безработный"
    salary:int|None = 0
    power:bp.BasePower|None = None
    fines: list[int] = []

