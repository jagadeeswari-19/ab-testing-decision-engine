import numpy as np
from scipy.stats import beta

def bayesian_prob(control_conv, control_total, treat_conv, treat_total):
    a_c, b_c = control_conv + 1, control_total - control_conv + 1
    a_t, b_t = treat_conv + 1, treat_total - treat_conv + 1

    samples_c = beta(a_c, b_c).rvs(5000)
    samples_t = beta(a_t, b_t).rvs(5000)

    return float((samples_t > samples_c).mean())