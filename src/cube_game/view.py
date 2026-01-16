import pygame
from typing import Tuple

class GameView:
    """Handles Pygame rendering in pixel units."""

    def __init__(self, width=400, height=400):
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Cube Game")
        self.clock = pygame.time.Clock()

    def clear(self) -> None:
        self.screen.fill((0, 0, 0))

    def draw_rect(self, position: Tuple[int, int], size: int, color=(255, 0, 0)) -> None:
        x, y = position
        pygame.draw.rect(self.screen, color, pygame.Rect(int(x), int(y), int(size), int(size)))

    def draw_cube(self, cube, color=(255, 0, 0)) -> None:
        """Draw a cube-model directly (expects pixel units)."""
        x, y, _ = cube.position
        size_px = int(cube.size)
        pygame.draw.rect(self.screen, color, pygame.Rect(int(x), int(y), size_px, size_px))

    def update(self) -> None:
        pygame.display.flip()
        self.clock.tick(60)
