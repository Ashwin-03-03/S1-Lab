import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt

# Example: dy/dx = -2y, y(0)=1
def f(t, y): return -2*y

sol = solve_ivp(f, (0, 5), [1])
plt.plot(sol.t, sol.y[0])
plt.show()
