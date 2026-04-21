def make_decision(lift, impact):

    if lift > 0 and impact > 0:
        return "STRONG ROLLOUT", "Positive lift with strong revenue impact"
    elif lift > 0:
        return "TEST FURTHER", "Slight improvement, needs validation"
    else:
        return "DO NOT ROLLOUT", "Negative performance detected"