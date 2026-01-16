# main.py

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# =========================
# MAP & PLANNING
# =========================
from maps.grid import grid, START, GOAL
from planning.astar import astar

# =========================
# ROBOT & CONTROL
# =========================
from model.differential import DifferentialDrive
from tracking.pure_pursuit import PurePursuit
from control.controller import DifferentialController

# =========================
# SIMULATION
# =========================
from simulation.simulator import Simulator

# =========================
# VISUALIZATION
# =========================
from visualization.plot_path import plot_path
from visualization.plot_error import plot_error
from visualization.animate_robot import animate_robot

from simulation.evaluation import print_simulation_summary

def main():

    # =========================
    # 1. PATH PLANNING (GRID)
    # =========================
    path_grid = astar(grid, START, GOAL)

    if path_grid is None:
        print("❌ PATH NOT FOUND")
        return

    # =========================
    # 2. GRID → WORLD (NO FLIP)
    # =========================
    # path_grid : (row, col)
    path = [(col, row) for row, col in path_grid]

    # =========================
    # 3. ROBOT MODEL
    # =========================
    x0, y0 = path[0]   # col, row

    robot = DifferentialDrive(
        x=x0,
        y=y0,
        theta=0.0
    )

    # =========================
    # 4. TRACKER & CONTROLLER
    # =========================
    tracker = PurePursuit(
        path,
        lookahead_distance=1.5
    )

    controller = DifferentialController()

    # =========================
    # 5. SIMULATION
    # =========================
    sim = Simulator(
        robot=robot,
        tracker=tracker,
        controller=controller,
        dt=0.1,
        max_time=200
    )

    history = sim.run()

    # =========================
    # PRINT RESULT (TERMINAL)
    # =========================
    goal_xy = path[-1]
    print_simulation_summary(
        history,
        goal=goal_xy,
        lookahead=tracker.Ld
    )

    # =========================
    # 6. VISUALIZATION
    # =========================
    plot_path(grid, path_grid, history)
    plot_error(history)
    animate_robot(grid, path_grid, history)


if __name__ == "__main__":
    main()
