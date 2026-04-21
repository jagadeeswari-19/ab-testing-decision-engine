import numpy as np
from scipy.stats import chisquare

def check_srm(control_n, treatment_n):
    observed = [control_n, treatment_n]
    expected = [np.mean(observed)] * 2
    _, p = chisquare(observed, expected)
    return p < 0.05