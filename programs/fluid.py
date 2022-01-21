from open_imagilib.emulator import *


# ---

def new_matrix():
    return [[0.] * 10 for _ in range(10)]


class Fluid:

    def __init__(self) -> None:

        # Fluid surface grid cells for numerical approximation
        self.p = new_matrix()
        self.v = new_matrix()

        # Temporary buffer of surface forces (allocated once)
        self.f = new_matrix()

    def step(self, time_step, co):

        p = self.p
        v = self.v
        f = self.f

        # Calculate surface tension forces
        s = 1 / 6
        for y in range(1, 9):
            for x in range(1, 9):
                f[y][x] = co * (
                    s * (
                        p[y - 1][x] +
                        p[y + 1][x] +
                        p[y][x - 1] +
                        p[y][x + 1] +
                        0.5 * (
                            p[y - 1][x - 1] +
                            p[y - 1][x + 1] +
                            p[y + 1][x - 1] +
                            p[y + 1][x + 1]
                        )
                    ) - p[y][x]
                )

        # Apply forces and advance positions
        for y in range(1, 9):
            for x in range(1, 9):
                v[y][x] = vv = v[y][x] + co * f[y][x] * time_step
                p[y][x] += vv * time_step

    def draw(self, matrix, amplification=1.0):
        amp = amplification * 116
        p = self.p
        for y in range(8):
            for x in range(8):
                v = max(0, min(255, int(round(140 + amp * p[1 + y][1 + x]))))
                matrix[y][x] = (0, v, 128 + (v >> 1))


# Initial conditions
w = Fluid()
w.p[1][1] = 1
w.p[1][8] = -1
w.p[8][1] = -1
w.p[8][8] = 1

# Simulate the time evolution and render frames
a = Animation()
for t in range(100):
    w.step(0.3, 1.0)
    w.draw(m, 2.5)
    a.add_frame(m, 33)

# ---

render(path='fluid.gif')
render()
