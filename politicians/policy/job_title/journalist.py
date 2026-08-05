import politicians.policy.powers.propaganda_activities as p
import politicians.policy.powers.base_power as bp
import politicians.policy.job_title.base_job_title as bjt

class Journalist(bjt.BaseJobTitle):
    name:str|None = "журналист"
    salary:int|None = 1_500
    power:bp.BasePower|None = p.PropagandaActivities()
    fines: list[int] = []
