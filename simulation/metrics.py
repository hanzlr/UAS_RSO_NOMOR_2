# simulation/metrics.py

import math


def cross_track_error(position, path):
    """
    Jarak minimum robot ke path
    position : (x, y)
    path     : list of (x, y)
    """

    x, y = position
    min_dist = float("inf")

    for px, py in path:
        d = math.hypot(x - px, y - py)
        if d < min_dist:
            min_dist = d

    return min_dist
