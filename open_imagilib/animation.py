""" Animation
"""
__all__ = ['Frame', 'Animation']

from dataclasses import dataclass

from .colors import Color, on, off
from .matrix import Matrix


@dataclass
class Frame:
    snapshot: Matrix
    duration: int


class Animation(list):
    min_duration = 25
    max_duration = 16777215

    default_instance = None

    def __init__(self, loop_count: int = 0) -> None:
        super().__init__()

        self.loop_count = loop_count

        if Animation.default_instance is None:
            Animation.default_instance = self

    def clear(self) -> None:
        self.loop_count = 0
        del self[:]

    def add_frame(self, matrix: Matrix, duration: int = 500) -> None:

        if duration < self.min_duration:
            duration = self.min_duration

        if duration > self.max_duration:
            duration = self.max_duration

        snapshot = Matrix(matrix)
        self.append(Frame(snapshot, duration))

    def scrolling_text(self, matrix: Matrix, text: str, text_color: Color = on, back_color: Color = off, duration: int = 80, loop_count: int = 0) -> None:
        self.loop_count = loop_count

        if not text:
            matrix.background(back_color)
            return

        text_len = len(text)
        for index in range(text_len):

            next_index = index + 1
            if next_index >= text_len:
                next_index = 0

            matrix.background(back_color)
            matrix.character(text[index], text_color)
            self.add_frame(matrix, duration)

            for offset in range(1, 8):
                matrix.background(back_color)
                matrix.character(text[index], text_color, x_offset=-offset)
                matrix.character(text[next_index], text_color, x_offset=8 - offset)
                self.add_frame(matrix, duration)
