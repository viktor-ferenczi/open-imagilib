from helpers import BaseTestCase
from open_imagilib.emulator import *


# noinspection PyShadowingNames
class TestBasics(BaseTestCase):

    def setUp(self) -> None:
        super().setUp()
        Animation.default_instance.clear()
        clear()

    def test_colors(self) -> None:

        m[0][0] = R
        m[0][1] = G
        m[0][2] = B
        m[0][3] = A
        m[0][4] = Y
        m[0][5] = O
        m[0][6] = M
        m[0][7] = P
        m[1][0] = W
        m[1][1] = K
        m[1][2] = on
        m[1][3] = off

        render(path='test_colors.png')
        self.verify_image('test_colors')

    def test_indoor(self) -> None:

        outdoor_mode = False

        m[0][0] = R
        m[0][1] = G
        m[0][2] = B
        m[0][3] = A
        m[0][4] = Y
        m[0][5] = O
        m[0][6] = M
        m[0][7] = P
        m[1][0] = W
        m[1][1] = K
        m[1][2] = on
        m[1][3] = off

        render(outdoor_mode=outdoor_mode, path='test_colors_indoor.png')
        self.verify_image('test_colors_indoor')

    def test_clear(self) -> None:

        for i in range(8):
            for j in range(8):
                m[i][j] = (i, j, i + j)

        clear()

        render(path='test_clear.png')
        self.verify_image('test_clear')

    def test_character(self) -> None:

        character('Y', Y)
        render(path='test_character.png')
        self.verify_image('test_character')

    def test_character_with_background(self) -> None:

        character('M', M, Y)
        render(path='test_character_with_background.png')
        self.verify_image('test_character_with_background')

    def test_character_overdraw(self) -> None:

        character('-', R)
        character('|', G)
        render(path='test_character_overdraw.png')
        self.verify_image('test_character_overdraw')

    def test_character_empty(self) -> None:

        character('', W)
        render(path='test_character_empty.png')
        self.verify_image('test_character_empty')

    def test_character_not_ascii(self) -> None:

        character('\t', W)
        render(path='test_character_not_ascii.png')
        self.verify_image('test_character_not_ascii')

