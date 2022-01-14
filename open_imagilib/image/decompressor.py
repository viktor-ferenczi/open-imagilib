# Image as Compressed Text version 1 (RLE)
MAGIC = 'ICT1'
VALUES = '_.:-+=abcdefghijklmnopqrstuvwxyz'
CODES = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ~?!@#$%&*/()[]{}<>'
REPEATS = ' 1234567890'


def decompress(text):
    w = h = x = y = 0
    p = (0, 0, 0)
    codes = {}
    rows = []
    for line in text:

        if not w:
            magic, w, h, line = line.split('|', 3)
            assert magic == MAGIC
            w, h = int(w), int(h)
            assert 0 < w <= 1000
            assert 0 < h <= 1000
            rows = [[] for _ in range(h)]

        if y >= h:
            break

        i = 0
        while i < len(line):
            c = line[i]
            i += 1

            if c in VALUES:
                r = VALUES.index(c) << 3
                g = VALUES.index(line[i]) << 3
                b = VALUES.index(line[i + 1]) << 3
                i += 2
                p = (r, g, b)
                repeats = 1
            elif c in codes:
                p = codes[c]
                repeats = 1
            elif c in CODES:
                codes[c] = p
                continue
            elif c in REPEATS:
                repeats = REPEATS.index(c)
            elif c == '^':
                repeats = int(line[i] + line[i + 1])
                i += 2
            else:
                continue

            for j in range(repeats):
                rows[y].append(p)
                x += 1
                if x == w:
                    x = 0
                    y += 1

        assert i == len(line)

    assert x == 0
    assert y == h

    return rows
