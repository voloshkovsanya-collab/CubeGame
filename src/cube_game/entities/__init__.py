"""
Підпакет entities.

Містить всі кубоподібні обʼєкти:
- ParentCube (базовий)
- Cube (гравець)
- Enemy (ворог)
"""

# Зручно робити імпорт класів прямо з пакета
from .parent_cube import ParentCube
from .cube import Cube
from .enemy import Enemy
