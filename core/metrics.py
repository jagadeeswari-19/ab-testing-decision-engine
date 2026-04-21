def calculate_metrics(df):
    control = df[df["group_name"] == "control"]
    treatment = df[df["group_name"] == "treatment"]

    cr_c = control["converted"].mean()
    cr_t = treatment["converted"].mean()

    lift = cr_t - cr_c

    return cr_c, cr_t, lift, len(control), len(treatment)