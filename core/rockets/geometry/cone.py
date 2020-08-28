from numpy import pi
from typing import Union

from .geometry import Geometry


class Cone(Geometry):
    """Геометрия конуса (полного и усеченного)."""

    def __init__(self,
                 d1: Union[int, float],
                 d2: Union[int, float],
                 height: Union[int, float]):
        self.checkSize(d1, d2, height)
        self._name = "Конус"
        self._d1, self._d2, self._h = d1, d2, height

    def __repr__(self):
        return f"Тело '{self._name}':" \
               f"\n - диаметр основания #1 d1 = {self._d1}" \
               f"\n - диаметр основания #2 d2 = {self._d2}" \
               f"\n - высота h = {self._h}" \
               f"\n - объём V = {self.volume}"

    @property
    def size(self) -> dict:
        return {'d1': self._d1, 'd2': self._d2, 'h': self._h, 'volume': self.volume}

    @property
    def volume(self) -> float:
        return 1/12*pi*self._h*(self._d1**2 + self._d2**2 + self._d1*self._d2)

    @property
    def diameterOne(self) -> float:
        return self._d1

    @diameterOne.setter
    def diameterOne(self, d1: float):
        if d1 >= 0:
            self._d1 = d1

    @property
    def diameterTwo(self) -> float:
        return self._d2

    @diameterTwo.setter
    def diameterTwo(self, d2: float):
        if d2 >= 0:
            self._d2 = d2

    @property
    def height(self) -> float:
        return self._h

    @height.setter
    def height(self, h: float):
        if h > 0:
            self._h = h
