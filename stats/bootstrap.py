import numpy as np

def bootstrap(control, treatment, n=500):
    diffs = []
    control = control.values
    treatment = treatment.values

    for _ in range(n):
        c = np.random.choice(control, size=len(control), replace=True).mean()
        t = np.random.choice(treatment, size=len(treatment), replace=True).mean()
        diffs.append(t - c)

    return np.array(diffs)