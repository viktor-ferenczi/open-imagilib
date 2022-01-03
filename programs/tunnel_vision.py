from open_imagilib.emulator import *

# ---

from math import sqrt

a = Animation()

def draw_tunnel(color):

    duration = 25
    speed = 3 / duration

    for t in range(duration):

        for i in range(8):
            y = i - 3.5

            for j in range(8):
                x = j - 3.5

                r = sqrt(x * x + y * y)

                r1 = speed * t - 3
                r2 = speed * t
                r3 = speed * t + 3

                v1 = 1 - (r - r1) ** 2
                v2 = 1 - (r - r2) ** 2
                v3 = 1 - (r - r3) ** 2

                v = max(v1, v2, v3)
                v = max(0, min(1, v))

                r = int(color[0] * v + 0.5)
                g = int(color[1] * v + 0.5)
                b = int(color[2] * v + 0.5)

                m[i][j] = (r, g, b)

        a.add_frame(m, 25)

draw_tunnel(M)

# ---

render(path='tunnel_vision.gif')
render()
