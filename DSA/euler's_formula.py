import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_xlim(-1.5, 1.5)
ax.set_ylim(-1.5, 1.5)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("Visualizing Euler’s Formula: $e^{ix} = \\cos(x) + i\\sin(x)$")

# Draw unit circle
theta = np.linspace(0, 2*np.pi, 500)
ax.plot(np.cos(theta), np.sin(theta), color='lightgray', linewidth=2, label='Unit Circle')

# Initialize point and line
point, = ax.plot([], [], 'ro', label='e^{ix}')
line, = ax.plot([], [], 'r--', alpha=0.5)

# Text annotation
text = ax.text(-1.4, 1.3, '', fontsize=12)

def init():
    point.set_data([], [])
    line.set_data([], [])
    text.set_text('')
    return point, line, text

def animate(x):
    # Compute complex exponential e^(ix)
    y = np.exp(1j * x)
    point.set_data(np.real(y), np.imag(y))
    line.set_data([0, np.real(y)], [0, np.imag(y)])
    
    # Display current angle and coordinates
    text.set_text(f"x = {x:.2f} rad\n"
                  f"Re = {np.real(y):.2f}, Im = {np.imag(y):.2f}")
    
    # Highlight when x = pi
    if abs(x - np.pi) < 0.05:
        ax.set_title("At x = π → $e^{iπ} = -1$ → Euler’s Identity!")
    else:
        ax.set_title("Visualizing Euler’s Formula: $e^{ix} = \\cos(x) + i\\sin(x)$")
    return point, line, text

# Create animation
ani = animation.FuncAnimation(
    fig, animate, frames=np.linspace(0, 2*np.pi, 200),
    init_func=init, blit=True, interval=50
)

plt.legend()
plt.show()
