# simulation/evaluation.py

import numpy as np
import math


def print_simulation_summary(history, goal=None, lookahead=1.0):
    time = np.array(history["time"])
    cte = np.array(history["cte"])
    v = np.array(history["v"])
    x = np.array(history["x"])
    y = np.array(history["y"])

    total_time = time[-1] if len(time) > 0 else 0.0
    steps = len(time)

    # ===== ERROR METRICS =====
    max_cte = np.max(cte)
    mean_cte = np.mean(cte)
    final_cte = cte[-1]

    # ===== PERCENTAGE ERROR =====
    max_cte_pct = (max_cte / lookahead) * 100.0
    mean_cte_pct = (mean_cte / lookahead) * 100.0
    final_cte_pct = (final_cte / lookahead) * 100.0

    print("\n========== SIMULATION SUMMARY ==========")
    print(f"Total steps           : {steps}")
    print(f"Total simulation time : {total_time:.2f} s")
    print(f"Average speed         : {np.mean(v):.3f} m/s")

    print("\n---------- TRACKING ERROR --------------")
    print(f"Max CTE               : {max_cte:.4f} m")
    print(f"Mean CTE              : {mean_cte:.4f} m")
    print(f"Final CTE             : {final_cte:.4f} m")

    print("\n------ TRACKING ERROR (%) --------------")
    print(f"Max Error (%)         : {max_cte_pct:.2f} %")
    print(f"Mean Error (%)        : {mean_cte_pct:.2f} %")
    print(f"Final Error (%)       : {final_cte_pct:.2f} %")

    if goal is not None:
        gx, gy = goal
        final_dist = math.hypot(x[-1] - gx, y[-1] - gy)
        goal_pct = (final_dist / lookahead) * 100.0

        print("\n---------- GOAL ERROR ------------------")
        print(f"Final distance to goal: {final_dist:.4f} m")
        print(f"Goal error (%)        : {goal_pct:.2f} %")
        print("Goal reached          :", "YES" if final_dist < 0.5 else "NO")

    print("========================================\n")
