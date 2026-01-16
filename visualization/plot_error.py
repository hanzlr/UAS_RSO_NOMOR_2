# visualization/plot_error.py

import matplotlib.pyplot as plt


def plot_error(history):
    t = history["time"]
    cte = history["cte"]

    plt.figure()
    plt.plot(t, cte)
    plt.grid(True)
    plt.title("Cross Track Error")
    plt.xlabel("Time [s]")
    plt.ylabel("Error [m]")
    plt.show()
