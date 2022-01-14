import os
from typing import Iterable, List, Dict, Callable

import cv2
import numpy as np


# Image as Compressed Text version 1 (RLE)
MAGIC = 'ICT1'
VALUES = '_.:-+=abcdefghijklmnopqrstuvwxyz'
CODES = ' ABCDEFGHIJKLMNOPQRSTUVWXYZ~?!@#$%&*/()[]{}<>'
REPEATS = [''] + list('1234567890') + [f'^{n:02d}' for n in range(11, 100)]


def compress(img_path: str, txt_path: str, *, wrapper=None):
    if wrapper is None:
        wrapper = make_python_list_formatter(60)

    img = cv2.imread(img_path)

    with open(txt_path, 'wt') as f:
        for line in wrapper(compress_image(img)):
            print(line, file=f)


def make_python_list_formatter(margin: int):
    assert margin > 7
    wrapper = make_wrapper(margin - 7)

    def formatter(tokens: Iterable[str]) -> Iterable[str]:
        yield '['
        for line in wrapper(tokens):
            yield f'    {line!r},'
        yield ']'

    return formatter


def make_wrapper(margin: int) -> Callable[[Iterable[str]], Iterable[str]]:

    def wrapper(tokens: Iterable[str]) -> Iterable[str]:
        length = 0
        buffer = []
        for token in tokens:
            buffer.append(token)
            length += len(token)
            if not token or length >= margin:
                yield ''.join(buffer)
                buffer.clear()
                length = 0

    return wrapper


def compress_image(img: np.ndarray) -> Iterable[str]:
    h, w, c = img.shape
    assert c == 3

    pixels = list(convert_to_rgb(img))

    yield f'{MAGIC}|{w}|{h}|'
    yield from compress_to_tokens(pixels)
    yield '|'
    yield ''


def convert_to_rgb(img: np.ndarray) -> Iterable[str]:
    h, w, _ = img.shape

    def f(v):
        return VALUES[v >> 3]

    for y in range(h):
        for x in range(w):
            b, g, r = img[y, x]
            yield f(r) + f(g) + f(b)

    yield ''


def compress_to_tokens(pixels: List[str]) -> Iterable[str]:
    counts = sorted(count_pixels(pixels).items(), key=lambda t: t[1], reverse=True)

    coding = {
        p: c
        for c, (p, n)
        in zip(CODES, counts)
        if n > 1
    }

    codes = {}

    repeats = 0
    current = None
    for pixel in pixels:

        if pixel != current or repeats == len(REPEATS):

            if current in codes:
                yield codes[current]
            elif current is not None:
                yield current
                if current in coding:
                    code = CODES[len(codes)]
                    codes[current] = code
                    yield code

            if repeats > 1:
                yield REPEATS[repeats - 1]

            repeats = 0

        current = pixel
        repeats += 1


def count_pixels(pixels: List[str]) -> Dict[str, int]:
    counts = {}
    for p in pixels:
        counts[p] = counts.get(p, 0) + 1
    return counts
