# simulation/simulator.py

import math
from simulation.metrics import cross_track_error


class Simulator:
    def __init__(
        self,
        robot,
        tracker,
        controller,
        dt=0.1,
        max_time=300.0
    ):
        self.robot = robot
        self.tracker = tracker
        self.controller = controller
        self.dt = dt
        self.max_time = max_time

    def run(self):
        """
        Jalankan simulasi
        return: history (dict)
        """

        history = {
            "x": [],
            "y": [],
            "theta": [],
            "v": [],
            "omega": [],
            "cte": [],
            "time": []
        }

        t = 0.0

        while t < self.max_time:

            x, y, theta = self.robot.pose()

            # 1. Tracking → curvature
            curvature = self.tracker.compute_curvature(x, y, theta)

            # 2. Controller → v, omega
            v, omega = self.controller.compute_control(curvature)

            # 3. Update robot
            self.robot.step(v, omega, self.dt)

            # 4. Hitung error
            cte = cross_track_error((x, y), self.tracker.path)

            # 5. Simpan history
            history["x"].append(x)
            history["y"].append(y)
            history["theta"].append(theta)
            history["v"].append(v)
            history["omega"].append(omega)
            history["cte"].append(cte)
            history["time"].append(t)

            # Stop jika mendekati goal
            gx, gy = self.tracker.path[-1]
            if math.hypot(x - gx, y - gy) < 0.5:
                break

            t += self.dt

        return history
