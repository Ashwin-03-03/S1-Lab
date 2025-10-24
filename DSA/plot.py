import numpy as np
import matplotlib.pyplot as plt

g, L, dt = 9.81, 1.0, 0.01
theta, omega = np.pi/4, 0
t, thetas = 0, []

for _ in range(1000):
    alpha = -(g/L)*np.sin(theta)
    omega += alpha*dt
    theta += omega*dt
    thetas.append(theta)

plt.plot(thetas)
plt.show()
