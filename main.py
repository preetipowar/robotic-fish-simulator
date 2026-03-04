import numpy as np
import matplotlib.pyplot as plt
import copy
import os
from config import params
from simulation.simulator import run_simulation
print("RUNNING MAIN FILE")
frequencies = np.linspace(0.5, 5, 20)
speeds = []

for f in frequencies:

    p = copy.deepcopy(params)
    p["frequency"] = f

    velocity, _ = run_simulation(p)

    speeds.append(velocity[-1])

plt.figure()

plt.plot(frequencies, speeds)

plt.xlabel("Tail Beat Frequency (Hz)")
plt.ylabel("Swimming Speed (m/s)")
plt.title("Swimming Speed vs Tail Frequency")

os.makedirs("results", exist_ok=True)
plt.savefig("results/speed_vs_frequency.png", dpi=300)

plt.show()

max_index = np.argmax(speeds)

optimal_frequency = frequencies[max_index]
max_speed = speeds[max_index]

print("Optimal Frequency:", optimal_frequency, "Hz")
print("Maximum Speed:", max_speed, "m/s")

from visualization.animation import animate_fish

animate_fish(params)