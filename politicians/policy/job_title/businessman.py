import politicians.policy.powers as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Businessman(bjt.BaseJobTitle):
    name:str|None = "бизнесмен"
    salary:int|None = 5_000
    power:bp.BasePower|None = None
    fines: list[int] = []
