""" Emulation of the global namespace used by imagiCharm programs
"""
from typing import Optional

from .animation import Animation
from .colors import *
from .matrix import Matrix

blink_rate = 0
outdoor_mode = True

m = Matrix()

Animation()


def clear():
    m.background(off)


def character(char: str, char_color: Color = on, back_color: Color = 0) -> None:
    if back_color:

        if back_color == 0:
            back_color = off

        m.background(back_color)

    m.character(char, char_color)


def scrolling_text(text: str, text_color: Color = on, back_color: Color = off, duration: int = 80, loop_count: int = 0) -> None:
    Animation.default_instance.scrolling_text(m, text, text_color, back_color, duration, loop_count)


# noinspection PyShadowingNames
def render(animation: Animation = None, *, blink_rate: int = 0, outdoor_mode: bool = True, path: Optional[str] = None, scale: int = 8) -> None:
    from .renderer import OpenCvRenderer, FileRenderer

    if animation is None:
        animation = Animation.default_instance

    assert animation is not None

    if 0 < blink_rate < 4:
        duration = 500 // blink_rate
        animation.add_frame(m, duration)
        clear()
        animation.add_frame(m, duration)

    if not animation:
        animation.add_frame(m)

    brightness = 256 if outdoor_mode else 192

    if path is None:
        OpenCvRenderer(animation, brightness=brightness).show(scale)
    else:
        FileRenderer(animation, brightness=brightness).save(path, scale)


del Matrix
del Color
del Optional
