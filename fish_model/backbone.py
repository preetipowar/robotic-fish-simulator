import numpy as np

def fish_backbone(t, params):

    N = params["segments"]
    L = params["length"]
    f = params["frequency"]
    k = params["wave_number"]
    Amax = params["tail_amp"]

    x = np.linspace(L, 0, N)

    A = np.zeros_like(x)

    tail_start = 0.7 * L   # last 30% of body moves

    mask = x > tail_start
    A[mask] = Amax * ((x[mask] - tail_start) / (L - tail_start))**2

    y = A * np.sin(2 * np.pi * (f * t + k * x))
    x= -x
    return x, y
def tail_velocity(t, params):

    L = params["length"]
    f = params["frequency"]
    k = params["wave_number"]
    Amax = params["tail_amp"]

    # amplitude at tail
    A = Amax

    v = 2 * np.pi * f * A * np.cos(2 * np.pi * (f * t - k * L))

    return v