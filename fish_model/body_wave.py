import numpy as np

def amplitude(x, A0=0.01, A1=0.02, A2=0.03):
    return A0 + A1*x + A2*(x**2)

def body_wave(x, t, f, k):
    A = amplitude(x)
    return A * np.sin(2*np.pi*(f*t - k*x))