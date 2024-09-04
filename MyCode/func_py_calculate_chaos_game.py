# func_py_calculate_chaos_game.py
import matplotlib.pyplot as plt
import random

def func_py_calculate_chaos_game(vertices, points, steps):
    x, y = [0], [0]
    for _ in range(steps):
        vx, vy = random.choice(vertices)
        x.append((x[-1] + vx) / 2)
        y.append((y[-1] + vy) / 2)
    plt.scatter(x, y, s=1)
    plt.title("Chaos Game")
    plt.show()

vertices = [(0, 0), (1, 0), (0.5, np.sqrt(3)/2)]
func_py_calculate_chaos_game(vertices, (0, 0), 10000)
