import politicians.policy.characteristics as ch
import politicians.policy.characteristics.paranoia as paranoia
import politicians.policy.characteristics.charisma as charisma
import politicians.policy.characteristics.erudition as erudition
import politicians.policy.characteristics.caution as caution
import politicians.policy.characteristics.good_health as good_health
import politicians.policy.characteristics.poor_health as poor_health
import politicians.policy.characteristics.generosity as generosity
import politicians.policy.characteristics.vindictiveness as vindictiveness
import politicians.policy.characteristics.lawyer as lawyer
import politicians.policy.characteristics.technophobe as technophobe
import politicians.policy.characteristics.lisp_speech as lisp_speech
import politicians.policy.characteristics.clever as clever
import politicians.policy.characteristics.stupid as stupid

data = {
    "paranoia": paranoia.Paranoia,
    "charisma": charisma.Charisma,
    "erudition": erudition.Erudition,
    "caution": caution.Caution,
    "good_health": good_health.GoodHealth,
    "poor_health": poor_health.PoorHealth,
    "generosity": generosity.Generosity,
    "vindictiveness": vindictiveness.Vindictiveness,
    "lawyer": lawyer.Lawyer,
    "technophobe": technophobe.Technophobe,
    "lisp_speech": lisp_speech.LispSpeech,
    "clever": clever.Clever,
    "stupid": stupid.Stupid
}

def str_to_characteristic(val:str) -> ch.characteristic.Characteristic:
    if val not in data:
        raise ValueError(f"Unknown characteristic: {val}")
    return data[val]()