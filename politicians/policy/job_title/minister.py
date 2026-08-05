import politicians.policy.powers.executive_branch as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Minister(bjt.BaseJobTitle):
    name:str|None = "министр"
    salary:int|None = 7_000
    power:bp.BasePower|None = p.ExecutiveBranch()
    fines: list[int] = []


