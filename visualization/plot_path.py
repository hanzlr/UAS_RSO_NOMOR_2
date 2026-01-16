# visualization/plot_path.py

import matplotlib.pyplot as plt


def plot_path(grid, path, history):

    px = [p[1] for p in path]   # col
    py = [p[0] for p in path]   # row

    rx = history["x"]
    ry = history["y"]

    plt.figure(figsize=(7, 7))

    # === SAME WITH THE TEST.PY ===
    plt.imshow(grid, cmap="gray_r", origin="lower")

    plt.plot(px, py, "b--", linewidth=2, label="Reference Path")
    plt.plot(rx, ry, "r", linewidth=2, label="Robot Trajectory")

    plt.scatter(px[0], py[0], c="red", s=80, label="Start")
    plt.scatter(px[-1], py[-1], c="blue", s=80, label="Goal")

    plt.xlim(0, grid.shape[1])
    plt.ylim(0, grid.shape[0])
    plt.gca().set_aspect("equal")
    plt.grid(True)
    plt.legend()
    plt.title("Path Tracking Result")
    plt.xlabel("X (column)")
    plt.ylabel("Y (row)")
    plt.show()
