import politicians.policy.powers.executive_branch as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Governor(bjt.BaseJobTitle):
    name:str|None = "губернатор"
    salary:int|None = 5_000
    power:bp.BasePower|None = p.ExecutiveBranch()
    importance = 8

