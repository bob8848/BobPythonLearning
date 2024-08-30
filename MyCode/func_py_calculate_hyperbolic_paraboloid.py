# func_py_calculate_hyperbolic_paraboloid.py
import matplotlib.pyplot as plt
import numpy as np

def func_py_calculate_hyperbolic_paraboloid(a, b, points):
    x = np.linspace(-a, a, points)
    y = np.linspace(-b, b, points)
    x, y = np.meshgrid(x, y)
    z = (x**2 / a**2) - (y**2 / b**2)
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    ax.plot_surface(x, y, z)
    plt.title("Hyperbolic Paraboloid")
    plt.show()

func_py_calculate_hyperbolic_paraboloid(5, 5, 100)
