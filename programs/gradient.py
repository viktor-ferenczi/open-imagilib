from open_imagilib.emulator import *

# ---

a = Animation()

COLORS = (
    (255, 0, 0),
    (0, 255, 0),
    (0, 0, 255),
    (255, 255, 255),
)

for r, g, b in COLORS:

    for i in range(64):

        y = i >> 3
        x = i & 7

        v = i << 2

        m[y][x] = (v & r, v & g, v & b)

    a.add_frame(m, 1000)

# ---

render(path='gradient.gif')
render()
