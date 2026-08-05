import politicians.policy.powers.propaganda_activities as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Blogger(bjt.BaseJobTitle):
    name:str|None = "блогер"
    salary:int|None = 3_000
    power:bp.BasePower|None = p.PropagandaActivities()
