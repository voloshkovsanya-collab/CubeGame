from cube_game.entities.parent_cube import ParentCube


class Enemy(ParentCube):
    """Enemy cube; positions and size in pixels.
    
    ПРИКЛАД self ДЛЯ ВОРОГА (ЕНЕМІ):
    enemy = Enemy(start_x_px=200, start_y_px=200)
    enemy.move(-5, 10)  →  self = enemy
                           self._position_px = позиція енемі
    
    ВЗАЄМОДІЯ self:
    cube.move(10, 20)   →  self = cube   (змінюється cube, не enemy)
    enemy.move(-5, 10)  →  self = enemy  (змінюється enemy, не cube)
    """
    def __init__(self, start_x_px: float = 0.0, start_y_px: float = 0.0, size_px: float = 50.0):
        super().__init__(size_px=size_px, position_px=(start_x_px, start_y_px, 0.0))
