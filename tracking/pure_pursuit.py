# tracking/pure_pursuit.py

import math
import numpy as np


class PurePursuit:
    def __init__(self, path, lookahead_distance=1.5):
        """
        path : list of (x, y) waypoints
        lookahead_distance : jarak lookahead
        """
        self.path = path
        self.Ld = lookahead_distance
        self.current_index = 0

    def compute_curvature(self, x, y, theta):
        """
        Input  : pose robot
        Output : curvature (kappa)
        """

        # Cari target point
        target = self.find_lookahead_point(x, y)

        if target is None:
            return 0.0

        tx, ty = target

        # Transform ke frame robot
        dx = tx - x
        dy = ty - y

        local_x = math.cos(theta) * dx + math.sin(theta) * dy
        local_y = -math.sin(theta) * dx + math.cos(theta) * dy

        if local_x == 0:
            return 0.0

        # Pure Pursuit curvature
        curvature = 2 * local_y / (self.Ld ** 2)
        return curvature

    def find_lookahead_point(self, x, y):
        """
        Cari waypoint pertama dengan jarak >= lookahead
        """
        for i in range(self.current_index, len(self.path)):
            px, py = self.path[i]
            dist = math.hypot(px - x, py - y)

            if dist >= self.Ld:
                self.current_index = i
                return px, py

        return None
