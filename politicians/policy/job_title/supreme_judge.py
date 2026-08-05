import politicians.policy.powers.judicial_branch as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class SupremeJudge(bjt.BaseJobTitle):
    name:str|None = "верховный судья"
    salary:int|None = 6_000
    power:bp.BasePower|None = p.JudicialBranch()
    fines: list[int] = []
