""" Renders the animation into a list of frames
"""
__all__ = ['OpenCvRenderer', 'FileRenderer']

from dataclasses import dataclass

import cv2
import imageio as iio
import numpy as np

from .animation import Frame, Animation

ESC = 27


@dataclass
class Options:
    brightness: int = 100
    cutoff: int = 0


@dataclass
class RenderedFrame:
    buffer: np.ndarray
    duration: int

    def __init__(self, frame: Frame, options: Options) -> None:
        buffer = np.array(frame.snapshot, np.int32)[:, :, ::-1]

        if 0 < options.cutoff < 256:
            buffer[buffer < options.cutoff] = 0

        np.clip(buffer, 0, 255, out=buffer)

        if 0 <= options.brightness < 256:
            buffer *= options.brightness
            buffer >>= 8

        self.buffer = buffer.astype(np.uint8)
        self.duration = frame.duration

    def get_pixels(self, scale: int = 1) -> np.ndarray:
        if scale < 0:
            return self.buffer

        h, w, _ = self.buffer.shape
        return cv2.resize(self.buffer, (w * scale, h * scale), interpolation=cv2.INTER_NEAREST)


class Renderer(list):

    def __init__(self, animation: Animation, *, brightness: int = 256, cutoff: int = 0) -> None:
        self.loop_count = animation.loop_count
        options = Options(brightness, cutoff)
        super().__init__(RenderedFrame(frame, options) for frame in animation)


class OpenCvRenderer(Renderer):
    def show(self, scale: int = 8, title : str = 'imagiCharm Preview'):

        cv2.namedWindow(title)

        def is_window_visible():
            return cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) >= 1

        stop = False
        repeats = 0

        while 1:

            for frame in self:
                cv2.imshow(title, frame.get_pixels(scale))

                key = cv2.waitKey(frame.duration)
                if key == ESC or not is_window_visible():
                    stop = True
                    break

            if stop:
                break

            if self.loop_count == 0:
                continue

            repeats += 1
            if repeats >= self.loop_count:
                break

        cv2.destroyWindow(title)


class FileRenderer(Renderer):

    def save(self, path, scale: int = 8):
        lc_filename = path.lower()
        if lc_filename.endswith('.png'):
            if len(self) == 1:
                self.save_first_frame(path, scale)
            else:
                self.save_each_frame(path, scale)
        elif lc_filename.endswith('.gif'):
            self.save_animated_gif(path, scale)
        else:
            raise ValueError('Unknown image format, please save to PNG or GIF')

    def save_each_frame(self, path: str, scale: int):
        for i, frame in enumerate(self):
            cv2.imwrite(f'{path[:-4]}.{i:04d}.png', self[i].get_pixels(scale))

    def save_first_frame(self, path: str, scale: int):
        cv2.imwrite(path, self[0].get_pixels(scale))

    def save_animated_gif(self, path: str, scale: int):
        frames = [frame.get_pixels(scale)[:, :, ::-1] for frame in self]
        durations = [0.001 * frame.duration for frame in self]

        # https://buildmedia.readthedocs.org/media/pdf/imageio/stable/imageio.pdf
        iio.mimsave(path, frames, duration=durations, loop=self.loop_count)
