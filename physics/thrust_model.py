import numpy as np

def thrust_force(rho, tail_area, frequency, theta_dot, tail_length):

    v_tail = tail_length * theta_dot

    Ct = 4.0

    thrust = Ct * rho * tail_area * (v_tail**2)

    return thrust