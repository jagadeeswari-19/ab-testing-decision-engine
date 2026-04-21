import math

def z_test(p1, p2, n1, n2):
    p = (p1*n1 + p2*n2) / (n1+n2)
    se = math.sqrt(p*(1-p)*(1/n1 + 1/n2))

    return (p2 - p1) / se if se != 0 else 0