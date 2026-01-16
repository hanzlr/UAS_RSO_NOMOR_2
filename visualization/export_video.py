# visualization/export_video.py

import matplotlib
matplotlib.use("Agg")  # ⬅ NON-GUI BACKEND

import matplotlib.pyplot as plt
import matplotlib.animation as animation
from tqdm import tqdm


def export_robot_video(
    grid,
    path_grid,
    history,
    filename="robot_tracking.mp4",
    fps=20
):
    print("🎬 Mulai export video...")

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.set_title("Robot Path Tracking (Video)")

    # =========================
    # MAP
    # =========================
    ax.imshow(grid, cmap="gray_r", origin="lower")

    # =========================
    # REFERENCE PATH
    # =========================
    path_x = [col for row, col in path_grid]
    path_y = [row for row, col in path_grid]
    ax.plot(path_x, path_y, "r--", linewidth=2, label="Reference Path")

    # =========================
    # ROBOT & TRAJECTORY
    # =========================
    robot_dot, = ax.plot([], [], "bo", markersize=6, label="Robot")
    traj_line, = ax.plot([], [], "b-", linewidth=1)

    ax.set_xlim(0, grid.shape[1])
    ax.set_ylim(0, grid.shape[0])
    ax.set_aspect("equal")
    ax.grid(True)
    ax.legend()

    traj_x, traj_y = [], []

    # =========================
    # FRAME UPDATE (NO GUI)
    # =========================
    def draw_frame(i):
        x = history["x"][i]
        y = history["y"][i]

        traj_x.append(x)
        traj_y.append(y)

        robot_dot.set_data([x], [y])   # ⬅️ HARUS LIST
        traj_line.set_data(traj_x, traj_y)

    # =========================
    # VIDEO WRITER
    # =========================
    writer = animation.FFMpegWriter(
        fps=fps,
        metadata={"artist": "Robot Simulation"},
        bitrate=1800
    )

    # =========================
    # EXPORT + PROGRESS BAR
    # =========================
    with writer.saving(fig, filename, dpi=100):
        for i in tqdm(
            range(len(history["x"])),
            desc="Exporting MP4",
            unit="frame"
        ):
            draw_frame(i)
            writer.grab_frame()

    plt.close(fig)
    print(f"✅ Export selesai: {filename}")
