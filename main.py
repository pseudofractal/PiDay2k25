import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, FFMpegWriter


N_SECONDS = 60
FPS = 60
N_FRAMES = N_SECONDS * FPS

catppuccin_mocha = {
    "base": "#1e1e2e",
    "text": "#cdd6f4",
    "overlay0": "#6c7086",
    "teal": "#94e2d5",
}

θ1 = 2 * np.pi * np.random.rand(N_FRAMES)
θ2 = 2 * np.pi * np.random.rand(N_FRAMES)
xs1 = np.cos(θ1)
ys1 = np.sin(θ1)
xs2 = np.cos(θ2)
ys2 = np.sin(θ2)
Ls = 2.0 * np.sin(np.abs(θ1 - θ2) / 2.0)

fig, ax = plt.subplots(figsize=(6, 6))
fig.patch.set_facecolor(catppuccin_mocha["base"])
ax.set_aspect("equal")
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis("off")
ax.set_facecolor(catppuccin_mocha["base"])


θ = np.linspace(0, 2 * np.pi, 300)
ax.plot(np.cos(θ), np.sin(θ), color=catppuccin_mocha["overlay0"], lw=4)

pi_text = ax.text(
    0, -1.3, "", ha="center", va="center", fontsize=12, color=catppuccin_mocha["text"]
)

lines = []
cumulative_length = 0.0


def init():
    pi_text.set_text("Estimated π: N/A")
    return lines + [pi_text]


def update(frame):
    global cumulative_length
    x1, y1, x2, y2, L = xs1[frame], ys1[frame], xs2[frame], ys2[frame], Ls[frame]
    (line,) = ax.plot(
        [x1, x2], [y1, y2], lw=0.1, color=catppuccin_mocha["teal"], alpha=0.2
    )
    lines.append(line)
    cumulative_length += L
    pi_est = 4.0 * (frame + 1) / cumulative_length
    pi_text.set_text(f"Estimated π: {pi_est:.10f}  (Chords: {frame + 1})")
    if frame % 100 == 0:
        print(f"({frame}/{N_FRAMES})")
    return lines + [pi_text]


print("Starting animation...")
anim = FuncAnimation(
    fig, update, frames=N_FRAMES, init_func=init, blit=True, repeat=True
)
plt.title("Estimating π via Random Chords", color=catppuccin_mocha["text"])
anim.save("animation.mp4", writer=FFMpegWriter(fps=FPS))
