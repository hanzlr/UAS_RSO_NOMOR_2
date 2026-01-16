# planning/path_utils.py

import numpy as np


def path_to_waypoints(path):
    """
    Convert grid path to float waypoints
    """
    return [(float(x), float(y)) for x, y in path]

def grid_to_xy(path, grid_shape):
    H = grid_shape[0]
    return [(c, H - 1 - r) for r, c in path]
