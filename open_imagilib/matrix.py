""" LED matrix
"""
__all__ = ['Matrix']

from .colors import Color, on, off
from .fonts import spectrum


class Matrix(list):

    def __init__(self, source=None) -> None:
        if source is None:
            row_iter = ([off for _ in range(8)] for _ in range(8))
        elif isinstance(source, list):
            row_iter = (list(row) for row in source)
        else:
            raise TypeError('Unknown source to build a Matrix from')

        super().__init__(row_iter)

    def background(self, color: Color) -> None:
        for i in range(8):
            for j in range(8):
                self[i][j] = color

    def character(self, char: str, char_color: Color = on, *, x_offset: int = 0) -> None:
        if x_offset <= -8 or x_offset >= 8:
            return

        if len(char) != 1 or char < ' ' or char > '\x7f':
            return

        bitmap = spectrum[ord(char) - 32]
        for i, row in enumerate(bitmap):
            for j, c in enumerate(row):
                if c != ' ':
                    x = x_offset + j
                    if 0 <= x < 8:
                        self[i][x] = char_color
