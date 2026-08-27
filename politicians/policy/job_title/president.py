import politicians.policy.powers.executive_branch as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class President(bjt.BaseJobTitle):
    name:str|None = "президент"
    salary:int|None = 10_000
    power:bp.BasePower|None = p.ExecutiveBranch()
    importance = 10
