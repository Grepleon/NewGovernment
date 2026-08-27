import politicians.policy.powers.executive_branch as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Mayor(bjt.BaseJobTitle):
    name:str|None = "мэр"
    salary:int|None = 3_000
    power:bp.BasePower|None = p.ExecutiveBranch()
    importance = 5

