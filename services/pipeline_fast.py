def run_pipeline_fast(df, aov=500, users=100000):

    # Fix column naming
    if "group" in df.columns:
        df = df.rename(columns={"group": "group_name"})

    if "group_name" not in df.columns or "converted" not in df.columns:
        return {"error": "Missing required columns"}

    control = df[df["group_name"] == "control"]
    treatment = df[df["group_name"] == "treatment"]

    if len(control) == 0 or len(treatment) == 0:
        return {"error": "Both control and treatment required"}

    conv_c = int(control["converted"].sum())
    conv_t = int(treatment["converted"].sum())

    vis_c = len(control)
    vis_t = len(treatment)

    cr_c = conv_c / vis_c
    cr_t = conv_t / vis_t

    lift = cr_t - cr_c

    # Fast approximations
    risk = 1.0 if lift < 0 else 0.0
    prob = max(0.0, min(1.0, 0.5 + lift))

    impact = lift * users * aov

    if lift > 0 and impact > 0:
        decision = "STRONG ROLLOUT"
        explanation = "Treatment improves conversion rate"
    elif lift > 0:
        decision = "CONDITIONAL ROLLOUT"
        explanation = "Treatment slightly improves conversion rate"
    else:
        decision = "DO NOT ROLLOUT"
        explanation = "Treatment reduces conversion rate"

    return {
        "control_rate": cr_c,
        "treatment_rate": cr_t,
        "lift": lift,
        "risk": risk,
        "probability": prob,
        "impact": impact,
        "decision": decision,
        "explanation": explanation
    }