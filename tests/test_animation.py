from helpers import BaseTestCase
from open_imagilib.emulator import *


# noinspection PyShadowingNames
class TestAnimation(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        Animation.default_instance.clear()
        clear()

    def test_blink_rate(self) -> None:

        blink_rate = 2

        character('O', R)

        render(blink_rate=blink_rate, path='test_blink_rate.gif', scale=3)
        self.verify_gif('test_blink_rate')

    def test_scrolling_text(self) -> None:

        scrolling_text("Scrolling Text ", A)

        render(path='test_scrolling_text.gif', scale=1)
        self.verify_gif('test_scrolling_text')

    def test_scrolling_text_with_background(self) -> None:

        scrolling_text("Scrolling Text ", Y, B)

        render(path='test_scrolling_text_with_background.gif', scale=1)
        self.verify_gif('test_scrolling_text_with_background')

    def test_scrolling_text_single_character(self) -> None:

        scrolling_text("W", W)

        render(path='test_scrolling_text_single_character.png', scale=2)
        self.verify_animation('test_scrolling_text_single_character', 6)

    def test_scrolling_text_empty(self) -> None:

        scrolling_text("")

        render(path='test_scrolling_text_empty.png')
        self.verify_image('test_scrolling_text_empty')
