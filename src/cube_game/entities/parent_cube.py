import pygame
from typing import Tuple


class ParentCube:
    """
    Base class for cube-like objects.
    Position and size are in pixels.
    """

    def __init__(self, size_px: float, position_px: Tuple[float, float, float]) -> None:
        # Store internal values as floats in pixels
        self._size_px = float(size_px)
        self._position_px = (float(position_px[0]), float(position_px[1]), float(position_px[2]))

    @property
    def size(self) -> float:
        """Size in pixels."""
        return self._size_px

    @size.setter
    def size(self, value: float) -> None:
        self._size_px = float(value)

    @property
    def position(self) -> Tuple[float, float, float]:
        """Position in pixels (x, y, z)."""
        return self._position_px

    @position.setter
    def position(self, value: Tuple[float, float, float]) -> None:
        x, y, z = value
        self._position_px = (float(x), float(y), float(z))

    def move(self, dx_px: float, dy_px: float, dz_px: float = 0.0) -> None:
        """Move by dx/dy/dz in pixels."""
        x, y, z = self._position_px
        self._position_px = (x + dx_px, y + dy_px, z + dz_px)

    @property
    def rect(self) -> pygame.Rect:
        """Return the integer rectangle for this cube."""
        x, y, _ = self._position_px
        return pygame.Rect(int(x), int(y), int(self._size_px), int(self._size_px))

    @property
    def center(self) -> Tuple[int, int]:
        """Return the center point of the cube."""
        x, y, _ = self._position_px
        half = self._size_px / 2.0
        return (int(x + half), int(y + half))

    def collidepoint(self, point: Tuple[float, float]) -> bool:
        """Check whether the given point is inside this cube."""
        return self.rect.collidepoint(int(point[0]), int(point[1]))

    @property
    def volume(self) -> float:
        # Volume in pixel^3 (keeps semantics from original API)
        return (self._size_px) ** 3
