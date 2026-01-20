import pygame
from cube_game.entities.cube import Cube
from cube_game.entities.enemy import Enemy

# Створюємо гравця та ворога
player = Cube(start_x_px=50, start_y_px=50, size_px=50)
enemy = Enemy(start_x_px=200, start_y_px=200, size_px=50)

def run() -> None:
    """Головний цикл гри."""
    while True:
        keys = pygame.key.get_pressed()
        dx = dy = 0
        speed = getattr(player, "speed_px", getattr(player, "speed", 4))

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
            player.move(dx, dy, 0.0)

        # Future: enemy AI, collisions etc.
        if hasattr(enemy, "update"):
            try:
                enemy.update()
            except TypeError:
                pass
