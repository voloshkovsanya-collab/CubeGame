from cube_game.entities.parent_cube import ParentCube
from typing import Tuple


class Cube(ParentCube):
    """Player cube. Positions and size are in pixels.
    
    Пояснення про self: - метод містить self як 0-й параметр що? def move(self, arg1, arg2): ...
    objcube = Cube(start_x_px=50, start_y_px=50)
    Крок 1 — звичайний (те що ти пишеш):
    objcube.move(10, 20)
    Крок 2 — що реально відбувається під капотом:
    Cube.move(objcube, 10, 20)
    Чому так? Коли Python бачить крапку . то він автоматично каже:
    "Беру об'єкт зліва від крапки → передаю його як перший аргумент методу щоб знати який саме об'єкт..."
    """

    def __init__(self, start_x_px: float = 0.0, start_y_px: float = 0.0, size_px: float = 50.0):
        # size and position stored in pixels
        super().__init__(size_px=size_px, position_px=(start_x_px, start_y_px, 0.0))
        # pixels per update/frame
        self.speed_px = 4.0




