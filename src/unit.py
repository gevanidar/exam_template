from enum import Enum


class Unit(Enum):
    EMPTY = "."  # Tecken för en tom ruta
    WALL = "■"  # Tecken för en ogenomtränglig vägg
    ITEM = "?"
    PLAYER = "@"
