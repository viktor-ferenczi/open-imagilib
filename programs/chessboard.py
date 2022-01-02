from open_imagilib.emulator import *

# ---

def draw_chessboard(dark_color, light_color):

    for y in range(0, 8, 2):

        for x in range(0, 8, 2):

            m[y][x] = dark_color
            m[y][x+1] = light_color

            m[y+1][x] = light_color
            m[y+1][x+1] = dark_color


def draw_chessboard_other(dark_color, light_color):
    for y in range(8):
        for x in range(8):
            if (x ^ y) & 1 != 0:
                m[y][x] = light_color
            else:
                m[y][x] = dark_color


def multiply_color(color, opacity):
    r, g, b = color

    r = (r * opacity + 50) // 100
    g = (g * opacity + 50) // 100
    b = (b * opacity + 50) // 100

    return r, g, b


def add_color(color1, color2):
    r1, g1, b1 = color1
    r2, g2, b2 = color2

    r = r1 + r2
    g = g1 + g2
    b = b1 + b2

    return r, g, b


a = Animation()

def draw_chessboard_transition(dark_color1, dark_color2, light_color1, light_color2):
    for t in range(26):
        t = t * 4
        f = 100 - t
        d = add_color(
            multiply_color(dark_color1, t),
            multiply_color(dark_color2, f),
        )
        l = add_color(
            multiply_color(light_color1, t),
            multiply_color(light_color2, f),
        )
        draw_chessboard_other(d, l)
        a.add_frame(m, 50)


draw_chessboard_transition(A, M, Y, Y)
draw_chessboard_transition(M, A, Y, Y)

# ---

render(a, path='chessboard.gif')
render(a)
