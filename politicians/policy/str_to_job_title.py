import politicians.policy.job_title.base_job_title as bjt
import politicians.policy.job_title as jt
import politicians.policy.job_title.blogger as blogger
import politicians.policy.job_title.businessman as businessman
import politicians.policy.job_title.constitutional_court_judge as constitutional_court_judge
import politicians.policy.job_title.deputy as deputy
import politicians.policy.job_title.head_cb as head_cb
import politicians.policy.job_title.journalist as journalist
import politicians.policy.job_title.minister as minister
import politicians.policy.job_title.president as president
import politicians.policy.job_title.senator as senator
import politicians.policy.job_title.supreme_judge as supreme_judge
import politicians.policy.job_title.unemployed as unemployed
import politicians.policy.job_title.mayor as mayor
import politicians.policy.job_title.governor as governor
import politicians.policy.job_title.general as general

data = {
    "blogger": jt.blogger.Blogger,
    "businessman": jt.businessman.Businessman,
    "constitutional_court_judge": jt.constitutional_court_judge.ConstitutionalCourtJudge,
    "deputy": jt.deputy.Deputy,
    "head_cb": jt.head_cb.HeadCB,
    "journalist": jt.journalist.Journalist,
    "minister": jt.minister.Minister,
    "president": jt.president.President,
    "senator": jt.senator.Senator,
    "supreme_judge": jt.supreme_judge.SupremeJudge,
    "unemployed": jt.unemployed.Unemployed,
    "mayor": jt.mayor.Mayor,
    "governor": jt.governor.Governor,
    "general": jt.general.General
}

def str_to_job_title(val:str) -> bjt.BaseJobTitle:
    if val not in data:
        raise ValueError("Unknown job title")
    return data[val]()