from open_imagilib.emulator import *

# ---

palette = [
    (r & v, g & v, b & v)
    for r, g, b in [
        (0, 0, 255),
        (255, 0, 0),
        (255, 0, 255),
        (0, 255, 0),
        (0, 255, 255),
        (255, 255, 0),
        (255, 255, 255),
    ][::-1]
    for v in range(16, 256, 16)
] * 2


def draw_mandelbrot(matrix, c0, s):
    h = len(matrix)

    sx = s / h
    sy = complex(0, sx)

    for y in range(h):
        rc = c0 + sy * (y - 0.5 * (h - 1))

        for x in range(h):
            c = rc + sx * (x - 0.5 * (h - 1))

            z = c
            for i in range(len(palette)):
                z = z * z + c
                if z.real * z.real + z.imag * z.imag >= 4:
                    matrix[y][x] = palette[i]
                    break
            else:
                matrix[y][x] = K


def downscale(matrix, full):
    t = len(matrix)
    s = len(full) // t
    d = s * s
    for y in range(t):
        by = y * s
        for x in range(t):
            r = g = b = 0
            bx = x * s
            for i in range(s):
                for j in range(s):
                    rr, gg, bb = full[by + i][bx + j]
                    r += rr
                    g += gg
                    b += bb
            matrix[y][x] = (r // d, g // d, b // d)


def animate_mandelbrot(animation, c0, s):
    full = [[K] * 32 for _ in range(32)]
    for t in range(100):
        draw_mandelbrot(full, c0, s)
        downscale(m, full)
        animation.add_frame(m, 50)
        s *= 0.96


a = Animation()
c0 = -0.74516 + 0.11258j
s = 4e-3
animate_mandelbrot(a, c0, s)


# ---

def test():
    import cv2
    import numpy as np
    full = [[K] * 64 for _ in range(64)]
    matrix = [[K] * 32 for _ in range(32)]
    ts = s
    for i in range(100):
        draw_mandelbrot(full, c0, ts)
        downscale(matrix, full)
        cv2.imshow('Mandelbrot', np.array(matrix, np.uint8)[:, :, ::-1])
        cv2.waitKey(25)
        ts *= 0.96
    cv2.waitKey()


TEST = False
if TEST:
    test()
else:
    render(path='mandelbrot.gif')
    render()
