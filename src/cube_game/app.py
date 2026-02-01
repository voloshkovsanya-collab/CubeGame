import pygame
from cube_game.entities.cube import Cube
from cube_game.entities.enemy import Enemy


class GameApp:
    """Контролер логіки гри."""
    
    def __init__(self):
        """Ініціалізує гру з гравцем та ворогом."""
        # Створюємо гравця та ворога
        self.player = Cube(start_x_px=50, start_y_px=50, size_px=50)
        self.enemy = Enemy(start_x_px=200, start_y_px=200, size_px=50)
    
    def update(self) -> None:
        """Оновлює логіку гри кожний фрейм."""
        keys = pygame.key.get_pressed()
        dx = dy = 0
        speed = getattr(self.player, "speed_px", getattr(self.player, "speed", 4))

        if keys[pygame.K_LEFT]:
            dx -= speed
        elif keys[pygame.K_RIGHT]:
            dx += speed

        if keys[pygame.K_UP]:
            dy -= speed
        elif keys[pygame.K_DOWN]:
            dy += speed

        # Рухаємо гравця
        if dx != 0 or dy != 0:
            self.player.move(dx, dy, 0.0)

        # Future: enemy AI, collisions etc.
        if hasattr(self.enemy, "update"):
            try:
                self.enemy.update()
            except TypeError:
                pass
    
    def stop(self) -> None:
        """Зупиняє гру."""
        pass
