import math
def db_scale(intensity):
    I_men = 1e-12
    beta = 10 * math.log10(intensity / I_men)
    return round(beta)