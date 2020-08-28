from numpy import pi
from typing import Union

from core.rockets.geometry.geometry import Geometry


class Cylinder(Geometry):
    """Геометрия цилиндра."""
    def __init__(self, d: Union[int, float], length: Union[int, float]):
        self.checkSize(d, length)
        self._name = "Цилиндр"
        self._d = d
        self._l = length

    def __repr__(self):
        return f"Тело '{self._name}':" \
               f"\n - диаметр d = {self._d}" \
               f"\n - длина l = {self._l}" \
               f"\n - объем V = {self.volume}"

    @property
    def size(self) -> dict:
        return {'d': self._d, 'l': self._l}

    @property
    def volume(self) -> float:
        return 0.25 * pi * self._d**2 * self._l

    @property
    def diameter(self) -> float:
        return self._d

    @diameter.setter
    def diameter(self, d: float):
        if d > 0:
            self._d = d

    @property
    def length(self) -> float:
        return self._l

    @length.setter
    def length(self, length: float):
        if length > 0:
            self._l = length


# Test Drive
if __name__ == '__main__':
    c = Cylinder(10, 20)
    print(c)
    print(c.size)
