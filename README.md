# Animated $\pi$ Estimation with Random Chords – Pi Day 2025

This is just a simple project I put together for $\pi$ Day. It estimates $\pi$ by drawing random chords inside a circle. There's nothing complicated—just basic geometry and randomness.

Inspired by [Charles Pergiel](https://docs.google.com/document/d/1vii-AshuqPQ14yjkwJNxB6PXcmKewWb3RlOUMyDc5Zs/edit?tab=t.0).

Here's the idea: if you pick two random points on a circle and connect them with a chord, the average length of many chords can be used to approximate pi.

### Derivation of the formula:

Start with a circle of radius 1 (a unit circle). The length $L$ of a chord connecting two points on the circle separated by an angle $\Delta\theta$ is given by:

$$
L(\Delta\theta) = 2\sin\left(\frac{\Delta\theta}{2}\right)
$$

When points are chosen randomly around the circle, the angle difference $\Delta\theta$ is a uniform proabbility distribution between $0$ and $2\pi$:

$$
f(\Delta\theta) = \frac{1}{2\pi}
$$

To find the average chord length, we calculate the expected value:

$$
E[L] = \int_{0}^{2\pi} f L d(\Delta\theta) = \frac{1}{2\pi}\int_{0}^{2\pi} 2\sin\left(\frac{\Delta\theta}{2}\right)d(\Delta\theta)
$$

To evaluate this integral we perform a basic substitution.\
Let $u = \Delta\theta/2$, which means $d(\Delta\theta)=2\,du$, and when $\Delta\theta \in [0, 2\pi]$, $u \in [0, \pi]$:

$$
E[L] = \frac{1}{2\pi}\int_{0}^{\pi} 2\sin(u)\cdot 2\,du = \frac{2}{\pi}\int_{0}^{\pi}\sin(u)\,du
$$

We know:

$$
\int_{0}^{\pi}\sin(u)\,du = [-\cos(u)]_{0}^{\pi} = (-\cos(\pi)) - (-\cos(0)) = 2
$$

So, the expected length becomes:

$$
E[L] = \frac{2}{\pi}\times 2 = \frac{4}{\pi}
$$

Finally, rearrange to estimate pi:

$$
\pi = \frac{4}{E[L]}
$$

So, by averaging the chord lengths, we get a simple approximation for pi.

### How the code works:
1. Draws a circle with radius 1.
2. Picks random pairs of points on the circle.
3. Measures the chord lengths between points.
4. Estimates pi using the average length.

You'll need Python, NumPy, Matplotlib, Numba, and FFmpeg.

Install dependencies:
```pip
pip install numpy matplotlib
```

Run the program:
```bash
python main.py
```

It will save an mp4 video called `animation.mp4`.\
You can find a preview here.\
<video src="animation.mp4" width="500" height="500" controls></video>


Happy $\pi$ day.