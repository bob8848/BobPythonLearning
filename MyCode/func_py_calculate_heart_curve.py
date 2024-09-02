# func_py_calculate_heart_curve.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_heart_curve(a, points):
    t = np.linspace(0, 2 * np.pi, points)
    x = a * 16 * np.sin(t)**3
    y = a * (13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t))
    plt.plot(x, y)
    plt.title("Heart Curve")
    plt.show()

func_py_calculate_heart_curve(5, 1000)
