import matplotlib.pyplot as plt
from maps.grid import grid

plt.imshow(grid, cmap="gray_r", origin="lower")
plt.scatter(1, 1, c="red", s=100)       # START
plt.scatter(39, 39, c="blue", s=100)    # GOAL
plt.show()
