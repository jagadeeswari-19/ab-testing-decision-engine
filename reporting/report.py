def generate_summary(result):
    return f"""
    📊 Experiment Summary

    Lift: {result['lift']:.4f}
    P-value: {result['p_value']:.4f}
    Risk: {result['risk']:.2%}
    Bayesian Confidence: {result['bayesian_prob']:.2%}
    Estimated Impact: ₹{result['impact']:,.2f}

    👉 Final Decision: {result['decision']}
    """