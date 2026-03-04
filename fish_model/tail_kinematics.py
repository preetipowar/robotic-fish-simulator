import numpy as np

def tail_angle(t, params):

    f = params["frequency"]
    theta_max = params["tail_amp"]

    return theta_max * np.sin(2 * np.pi * f * t)