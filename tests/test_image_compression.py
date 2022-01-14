import cv2
import numpy as np

from helpers import BaseTestCase
from open_imagilib.image.compressor import compress
from open_imagilib.image.decompressor import decompress


class TestImageCompression(BaseTestCase):

    def test_compression(self) -> None:
        compress('data/olympics.png', 'olympics.txt')

        with open('olympics.txt', 'rt') as f:
            text = eval(f.read())

        decompressed = decompress(text)
        decompressed = np.array(decompressed, np.uint8)[:, :, ::-1]
        cv2.imwrite('olympics.png', decompressed)

        h, w, _ = decompressed.shape
        compressed_size = sum(map(len, text))
        pixel_count = h * w
        bits_per_pixel = 8 * compressed_size / pixel_count
        print(f'{bits_per_pixel:.2f} bits/pixel ({100 * bits_per_pixel / 24:.2f}%)')

        self.verify_image('olympics')
        self.verify_text_file('olympics')
