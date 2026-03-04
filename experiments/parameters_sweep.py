import numpy as np
import matplotlib.pyplot as plt
import copy

from config import params
from simulation.simulator import run_simulation

frequencies = np.linspace(0.5, 5, 20)

speeds = []
cost_of_transport = []
strouhal_numbers = []

g = 9.81

for f in frequencies:

    p = copy.deepcopy(params)
    p["frequency"] = f

    velocity, position = run_simulation(p)

    # steady swimming speed
    U = velocity[-1]
    speeds.append(U)

    # propulsion estimate
    rho = p["rho"]
    tail_area = p["tail_area"]
    tail_length = p["tail_length"]
    theta_amp = p["tail_amp"]

    theta_dot = 2 * np.pi * f * theta_amp
    v_tail = tail_length * theta_dot

    Ct = 4.0

    thrust = Ct * rho * tail_area * v_tail**2

    power = thrust * max(U, 1e-6)

    cot = power / (p["mass"] * g * max(U, 1e-6))
    cost_of_transport.append(cot)

    # Strouhal number
    A = theta_amp * tail_length
    St = (f * A) / max(U, 1e-6)

    strouhal_numbers.append(St)


print("Speed points:", len(speeds))
print("COT points:", len(cost_of_transport))
print("Strouhal points:", len(strouhal_numbers))


# ---------------- SPEED PLOT ----------------

plt.figure()

plt.plot(frequencies, speeds, marker="o")

plt.xlabel("Tail Beat Frequency (Hz)")
plt.ylabel("Swimming Speed (m/s)")
plt.title("Swimming Speed vs Tail Frequency")

plt.grid(True)


# ---------------- COST OF TRANSPORT ----------------

plt.figure()

plt.plot(frequencies, cost_of_transport, marker="o")

plt.xlabel("Tail Beat Frequency (Hz)")
plt.ylabel("Cost of Transport")
plt.title("Cost of Transport vs Tail Frequency")

plt.grid(True)


# ---------------- STROUHAL NUMBER ----------------

plt.figure()

plt.plot(frequencies, strouhal_numbers, marker="o")

plt.xlabel("Tail Beat Frequency (Hz)")
plt.ylabel("Strouhal Number")
plt.title("Strouhal Number vs Tail Frequency")

plt.grid(True)


plt.show()