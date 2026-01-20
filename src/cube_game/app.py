import pygame
from cube_game.entities.cube import Cube
from cube_game.entities.enemy import Enemy

class GameApp:
    """Controls game logic (positions/speeds are in pixels)."""

    def __init__(self):
        # Create player at pixel coordinates
        self.player = Cube(start_x_px=50, start_y_px=50, size_px=50)

        # Create an enemy for demonstration
        self.enemy = Enemy(start_x_px=200, start_y_px=200, size_px=50)

    def update(self) -> None:
        """Process input and update game entities (pixel units)."""
        keys = pygame.key.get_pressed()
        dx = dy = 0
        # self.player → гравець (Куб), до якого звертаємось через self цієї гри
        speed = getattr(self.player, "speed_px", getattr(self.player, "speed", 4))

        if keys[pygame.K_LEFT]:
            dx -= speed
        elif keys[pygame.K_RIGHT]:
            dx += speed

        if keys[pygame.K_UP]:
            dy -= speed
        elif keys[pygame.K_DOWN]:
            dy += speed

        # Apply movement to the player (use model API)
        # self.player.move_by(dx, dy) → рухаємо ГРАВЦЯ (Куба), не енемі!
        if dx != 0 or dy != 0:
            self.player.move_by(dx, dy)

        # Future: enemy AI, collisions etc.
        if hasattr(self.enemy, "update"):
            try:
                self.enemy.update()
            except TypeError:
                pass
