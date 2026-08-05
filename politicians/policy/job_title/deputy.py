import politicians.policy.powers.legislative_branch as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Deputy(bjt.BaseJobTitle):
    name:str|None = "депутат"
    salary:int|None = 5_000
    power:bp.BasePower|None = p.LegislativeBranch()
    fines: list[int] = []
