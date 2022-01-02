import os
import unittest

import cv2
import imageio as iio
import numpy as np


class BaseTestCase(unittest.TestCase):

    def verify_image(self, name: str, ext: str = 'png'):
        result = cv2.imread(f'{name}.{ext}')
        expected = cv2.imread(f'reference/{name}.{ext}')

        self.assertTrue(np.all(result == expected))

        os.remove(f'{name}.{ext}')

    def verify_animation(self, name: str, frame_count: int, ext: str = 'png'):
        for i in range(frame_count):
            self.verify_image(f'{name}.{i:04d}', ext)

        self.assertFalse(os.path.exists(f'{name}.{frame_count:04d}.{ext}'))

    def verify_gif(self, name: str):
        result = list(iio.get_reader(f'{name}.gif'))
        expected = list(iio.get_reader(f'reference/{name}.gif'))

        self.assertEqual(len(result), len(expected))

        for result_frame, expected_frame in zip(result, expected):
            self.assertTrue(np.all(result_frame == expected_frame))

        os.remove(f'{name}.gif')
