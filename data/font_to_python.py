from typing import Iterable

import cv2
import numpy as np


def image_to_python(name: str, png_filename: str) -> Iterable[str]:
    img: np.ndarray = cv2.imread(png_filename)

    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img = img < 128

    h, w = img.shape

    yield f'{name} = ('

    for y in range(0, h, 8):
        for x in range(0, w, 8):

            yield '    ('

            for i in range(8):
                row = ''.join(' #'[p] for p in img[y + i, x:x + 8])
                yield f'        {repr(row)},'

            yield '    ),'

    yield ')'


if __name__ == '__main__':
    for line in image_to_python('spectrum', 'ZX_Spectrum_character_set.png'):
        print(line)
