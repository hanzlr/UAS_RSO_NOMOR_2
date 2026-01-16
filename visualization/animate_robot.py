# visualization/animate_robot.py

import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


def animate_robot(grid, path, history):

    rx = history["x"]
    ry = history["y"]

    # =========================
    # WORLD → GRID (UNTUK PLOT MAP)
    # =========================
    h = grid.shape[0]
    px = [p[0] for p in path]
    py = [p[1] for p in path]

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title("Path Tracking Animation")

    # =========================
    # MAP
    # =========================
    ax.imshow(grid, cmap="gray_r", origin="upper")

    # =========================
    # REFERENCE PATH 
    # =========================
    ax.plot(py, px, "b--", linewidth=2, label="Reference Path")

    # =========================
    # ROBOT
    # =========================
    robot, = ax.plot([], [], "ro", markersize=6, label="Robot")
    traj, = ax.plot([], [], "r-", linewidth=1)

    ax.set_xlim(0, grid.shape[1])
    ax.set_ylim(0, grid.shape[0])
    ax.set_aspect("equal")
    ax.legend()
    ax.grid(True)

    def init():
        robot.set_data([], [])
        traj.set_data([], [])
        return robot, traj

    def update(i):
        robot.set_data([rx[i]], [ry[i]])
        traj.set_data(rx[:i+1], ry[:i+1])
        return robot, traj

    ani = FuncAnimation(
        fig,
        update,
        frames=len(rx),
        init_func=init,
        interval=50,
        blit=False
    )

    plt.show()
