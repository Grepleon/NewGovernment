import politicians.policy.powers.judicial_branch as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class ConstitutionalCourtJudge(bjt.BaseJobTitle):
    name:str|None = "конституционный судья"
    salary:int|None = 6_500
    power:bp.BasePower|None = p.JudicialBranch()

