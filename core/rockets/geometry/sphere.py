from numpy import pi
from typing import Union

from core.rockets.geometry.geometry import Geometry


class Sphere(Geometry):
    """Геометрия сферы (полной и сегмента)."""

    def __init__(self, d: Union[int, float], h: Union[int, float, None] = None):
        self.checkSize(d, h) if h else self.checkSize(d)
        self._name = "Сфера"
        self._d = d
        if h is None or h > d:
            self._h = d
        else:
            self._h = h

    def __repr__(self):
        s = f"Тело {self._name}:" \
            f"\n - диаметр d = {self._d}"
        if self._h != self._d:
            s += f"\n - высота сегмента h = {self._h}"
        s += f"\n - объем V = {self.volume}"
        return s

    @property
    def size(self) -> dict:
        return {'d': self._d, 'h': self._h}

    @property
    def volume(self) -> float:
        return pi * self._h**2 * (0.5*self._d - self._h / 3)

    @property
    def diameter(self) -> float:
        return self._d

    @diameter.setter
    def diameter(self, d: float):
        if d > 0:
            self._d = d

    @property
    def segmentHeight(self) -> float:
        return self._h

    @segmentHeight.setter
    def segmentHeight(self, h: float):
        if 0 <= h <= self._d:
            self._h = h
        else:
            self._h = self._d


# Test Drive
if __name__ == '__main__':
    s = Sphere(10, 2)
    print(s)
    print(s.size)

    s = Sphere(10)
    print(s)
    print(s.size)
