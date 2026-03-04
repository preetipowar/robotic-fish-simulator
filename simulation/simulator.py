from physics.thrust_model import thrust_force
from physics.drag_model import drag_force
from physics.dynamics import acceleration
from fish_model.tail_kinematics import tail_angle
import numpy as np


def run_simulation(params):

    dt = params["dt"]
    steps = params["steps"]

    v = 0.0
    x = 0.0

    velocity_log = []
    position_log = []

    for i in range(steps):

        # current simulation time
        t = i * dt

        # tail angle from kinematics
        theta = tail_angle(t, params)

        # angular velocity of the tail
        theta_dot = (
            2 * np.pi
            * params["frequency"]
            * params["tail_amp"]
            * np.cos(2 * np.pi * params["frequency"] * t)
        )

        # thrust force
        thrust = thrust_force(
            params["rho"],
            params["tail_area"],
            params["frequency"],
            theta_dot,
            params["tail_length"]
        )

        # hydrodynamic drag
        drag = drag_force(
            params["rho"],
            params["Cd"],
            params["body_area"],
            v
        )

        # compute acceleration
        a = acceleration(thrust, drag, params["mass"])

        # integrate velocity
        v = v + a * dt

        # integrate position
        x = x + v * dt

        velocity_log.append(v)
        position_log.append(x)

    return velocity_log, position_log