from core.metrics import calculate_metrics
from core.decision import make_decision
from core.logger import logger
from stats.frequentist import z_test
from db.models import save_experiment


def run_experiment(df, aov=500, users=100000):

    # Fix column naming
    if "group" in df.columns:
        df = df.rename(columns={"group": "group_name"})

    if "group_name" not in df.columns or "converted" not in df.columns:
        return {"error": "Missing required columns"}

    cr_c, cr_t, lift, n1, n2 = calculate_metrics(df)

    impact = lift * users * aov

    decision, explanation = make_decision(lift, impact)

    z = z_test(cr_c, cr_t, n1, n2)

    result = {
        "control_rate": cr_c,
        "treatment_rate": cr_t,
        "lift": lift,
        "z_score": z,
        "impact": impact,
        "decision": decision,
        "explanation": explanation
    }

    # Save to DB
    save_experiment(result)

    logger.info(f"Experiment result: {result}")

    return result