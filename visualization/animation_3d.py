import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from mpl_toolkits.mplot3d import Axes3D

from simulation.simulator import run_simulation
from fish_model.tail_kinematics import tail_angle


def animate_fish_3d(params):

    velocity, position = run_simulation(params)

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.set_xlim(-1, 3)
    ax.set_ylim(-1, 1)
    ax.set_zlim(-1, 1)

    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")

    ax.set_title("3D Robotic Fish Simulation")

    L = params["length"]
    body_len = 0.7 * L
    tail_len = 0.3 * L

    body_line, = ax.plot([], [], [], lw=4)
    tail_line, = ax.plot([], [], [], lw=4)


    def update(frame):

        t = frame * params["dt"]
        theta = tail_angle(t, params)

        x_offset = position[frame]

        # rigid body
        nose = np.array([body_len + x_offset, 0, 0])
        mid = np.array([0.5 * body_len + x_offset, 0, 0])
        joint = np.array([x_offset, 0, 0])

        # tail rotation
        tail = joint + np.array([
            -tail_len * np.cos(theta),
            tail_len * np.sin(theta),
            0
        ])

        body_x = [nose[0], mid[0], joint[0]]
        body_y = [nose[1], mid[1], joint[1]]
        body_z = [nose[2], mid[2], joint[2]]

        tail_x = [joint[0], tail[0]]
        tail_y = [joint[1], tail[1]]
        tail_z = [joint[2], tail[2]]

        body_line.set_data(body_x, body_y)
        body_line.set_3d_properties(body_z)

        tail_line.set_data(tail_x, tail_y)
        tail_line.set_3d_properties(tail_z)

        ax.set_xlim(x_offset - 1, x_offset + 2)

        return body_line, tail_line
        

    ani = FuncAnimation(
        fig,
        update,
        frames=len(position),
        interval=30,
        blit=False
    )
    ani.save("results/fish_swimming.gif", writer="pillow", fps=30)
    plt.show()