import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

from fish_model.tail_kinematics import tail_angle
from simulation.simulator import run_simulation


def animate_fish(params):

    velocity, position = run_simulation(params)

    fig, ax = plt.subplots(figsize=(10,4))

    line, = ax.plot([], [], lw=4)

    # wake particles
    wake_x = []
    wake_y = []
    wake_scatter = ax.scatter([], [], s=6, alpha=0.5)

    ax.set_ylim(-0.5, 0.5)
    ax.set_xlim(-1, 3)

    ax.set_xlabel("Position")
    ax.set_ylabel("Body Displacement")
    ax.set_title("Bio-Inspired Robotic Fish Swimming")

    L = params["length"]

    body_len = 0.7 * L
    tail_len = 0.3 * L


    def update(frame):

        t = frame * params["dt"]
        theta = tail_angle(t, params)

        x_offset = position[frame]

        # --- body points ---
        joint = np.array([0, 0])
        mid  = joint + np.array([body_len * 0.5, 0])
        nose = joint + np.array([body_len, 0])

        # --- tail rotation around joint ---
        tail = joint + np.array([
            -tail_len * np.cos(theta),
            tail_len * np.sin(theta)
        ])

        # fish body line
        x = [
            nose[0] + x_offset,
            mid[0] + x_offset,
            joint[0] + x_offset,
            tail[0] + x_offset
        ]

        y = [
            nose[1],
            mid[1],
            joint[1],
            tail[1]
        ]

        line.set_data(x, y)

        # ---------------- WAKE GENERATION ----------------

        # spawn particle at tail
        wake_x.append(tail[0] + x_offset)
        wake_y.append(tail[1])

        # move wake backward (water flow)
        for i in range(len(wake_x)):
            wake_x[i] -= 0.02

        # slight vortex oscillation
        for i in range(len(wake_y)):
            wake_y[i] += 0.002 * np.sin(frame * 0.2 + i)

        wake_scatter.set_offsets(np.column_stack((wake_x, wake_y)))

        # camera follows fish
        ax.set_xlim(x_offset - 1, x_offset + 2)

        return line, wake_scatter


    ani = FuncAnimation(
        fig,
        update,
        frames=len(position),
        interval=30,
        blit=False
    )
    ani.save("results/fish_swimming2d.gif", writer="pillow", fps=30)
    plt.show()