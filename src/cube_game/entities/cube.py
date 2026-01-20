from cube_game.entities.parent_cube import ParentCube
from typing import Tuple


class Cube(ParentCube):
    """Player cube. Positions and size are in pixels.
    
    ПРИКЛАД self ДЛЯ ГРАВЦЯ (КУБА):
    player_cube = Cube(start_x_px=50, start_y_px=50)
    player_cube.move_by(10, 20)  →  self = player_cube
                                     self.speed_px = 4.0 (гравця)
    """

    def __init__(self, start_x_px: float = 0.0, start_y_px: float = 0.0, size_px: float = 50.0):
        # size and position stored in pixels
        super().__init__(size_px=size_px, position_px=(start_x_px, start_y_px, 0.0))
        # pixels per update/frame
        self.speed_px = 4.0

    def move_by(self, dx_px: float, dy_px: float) -> None:
        """Move the cube by dx/dy in pixels (called by GameApp).
        
        self = цей куб (гравець)
        Рухаємо саме цей куб, не інший!
        """
        # self.move() → викликаємо метод батька для ЦЬОГО куба
        self.move(dx_px, dy_px, 0.0)




