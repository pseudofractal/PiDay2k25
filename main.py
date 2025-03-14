import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter
from numba import njit

catppuccin_mocha = {
    "base": "#1e1e2e",
    "text": "#cdd6f4",
    "overlay0": "#6c7086",
    "teal": "#94e2d5",
}


@njit
def compute_chord_length(theta1: float, theta2: float) -> float:
    return 2.0 * np.sin(np.abs(theta1 - theta2) / 2.0)


def generate_random_chord():
    theta1 = 2 * np.pi * np.random.rand()
    theta2 = 2 * np.pi * np.random.rand()
    x1, y1 = np.cos(theta1), np.sin(theta1)
    x2, y2 = np.cos(theta2), np.sin(theta2)
    L = compute_chord_length(theta1, theta2)
    return (x1, y1, x2, y2, L)


chords = []
chord_lengths = []

fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor(catppuccin_mocha["base"])
ax.set_aspect("equal")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis("off")
ax.set_facecolor(catppuccin_mocha["base"])

theta = np.linspace(0, 2 * np.pi, 300)
ax.plot(np.cos(theta), np.sin(theta), color=catppuccin_mocha["overlay0"], lw=4)

pi_text = ax.text(
    0, -1.3, "", ha="center", va="center", fontsize=12, color=catppuccin_mocha["text"]
)

lines = []


def init():
    pi_text.set_text("Estimated π: N/A")
    return lines + [pi_text]


def update(frame):

    x1, y1, x2, y2, L = generate_random_chord()
    chords.append((x1, y1, x2, y2))
    chord_lengths.append(L)

    (line,) = ax.plot(
        [x1, x2], [y1, y2], lw=3, color=catppuccin_mocha["teal"], alpha=0.6
    )
    lines.append(line)

    avg_length = np.mean(chord_lengths)
    pi_est = 4.0 / avg_length
    pi_text.set_text(f"Estimated π: {pi_est:.10f}  (Chords: {len(chord_lengths)})")

    return lines + [pi_text]


anim = FuncAnimation(
    fig, update, frames=1000, init_func=init, blit=True, interval=50, repeat=True
)
plt.title("Animated π Estimation via Random Chords", color=catppuccin_mocha["text"])


anim.save("animation.mp4", writer=FFMpegWriter(fps=20))