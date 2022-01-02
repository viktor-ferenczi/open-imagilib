from open_imagilib.emulator import *

# ---

from math import pi, sqrt, atan2

a = Animation()

# Based on colorsys.hsv_to_rgb
def hsv_to_rgb(h, s, v):
    if s == 0.0:
        v = int(255 * v + 0.5)
        return v, v, v

    h = (h % 360) * pi / 180

    i = int(h * 6.0)
    f = (h * 6.0) - i
    p = v * (1.0 - s)
    q = v * (1.0 - s * f)
    t = v * (1.0 - s * (1.0 - f))

    v = int(255 * v + 0.5)
    t = int(255 * t + 0.5)
    p = int(255 * p + 0.5)
    q = int(255 * q + 0.5)

    i = i % 6
    if i == 0:
        return v, t, p
    if i == 1:
        return q, v, p
    if i == 2:
        return p, v, t
    if i == 3:
        return p, q, v
    if i == 4:
        return t, p, v
    return v, p, q


for t in range(60):

    for i in range(8):
        y = i - 3.5

        for j in range(8):
            x = j - 3.5

            r = sqrt(x * x + y * y)
            p = atan2(y, x) * 90 / pi

            h = p + t * 6 - r * 10
            s = 1
            v = 1 - r / 8

            m[i][j] = hsv_to_rgb(h, s, v)

    a.add_frame(m, 50)

# ---

render(path='hsv_spiral.gif')
render()
