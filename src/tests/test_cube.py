import unittest

from cube_game.entities.cube import Cube


class TestCube(unittest.TestCase):
    def test_move_by_pixels(self):
        c = Cube(start_x_px=10, start_y_px=20, size_px=5)
        c.move_by(15, -5)
        self.assertEqual(c.position, (25.0, 15.0, 0.0))


if __name__ == "__main__":
    unittest.main()
