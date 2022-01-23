from open_imagilib.emulator import *

# ---

a = Animation()

BACKGROUND_COLOR = K
BALL_COLOR = W
PLAYER_COLOR = (160, 160, 160)
BRICK_COLORS = [R, G, B, Y, O, M, P, A]

background(BACKGROUND_COLOR)

total = 0
for y in range(2, 4):
    for x in range(0, 8, 2):
        c = BRICK_COLORS[total % len(BRICK_COLORS)]
        m[y][x] = m[y][x + 1] = c
        total += 1

px = 4
bx, by = px, 6
vx, vy = -1, -1
removed = 0

for _ in range(100):

    m[by][bx] = BACKGROUND_COLOR

    bx += vx
    by += vy

    if bx < 0:
        bx = 1
        vx = 1

    if bx > 7:
        bx = 6
        vx = -1

    if by < 0:
        by = 1
        vy = 1

    if by > 7:
        break

    if m[by][bx] == PLAYER_COLOR or m[by][bx - vx] == PLAYER_COLOR:
        by = 5
        vy = -1

    if m[by][bx] in BRICK_COLORS:
        x = bx & 6
        m[by][x] = m[by][x + 1] = BACKGROUND_COLOR
        removed += 1
        vy = -vy
        if 0 <= bx + vx < 8 and by + vy >= 0 and m[bx + vx][by + vy] in BRICK_COLORS:
            vx = -vx

    m[by][bx] = BALL_COLOR

    if by > 2:
        if px < 6 and bx > px:
            px += 1
        elif px > 1 and bx < px:
            px -= 1

    for x in range(8):
        m[7][x] = PLAYER_COLOR if px - 1 <= x <= px + 1 else BACKGROUND_COLOR

    finished = removed == total

    a.add_frame(m, 500 if finished else 50)

    if finished:
        break

# ---

render(path='arkanoid.gif')
render()
