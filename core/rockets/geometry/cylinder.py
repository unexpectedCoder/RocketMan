from numpy import pi
from typing import Union

from core.rockets.geometry.geometry import Geometry
from core.exceptions.exception import BodySizeException


class Cylinder(Geometry):
    """Геометрия цилиндра."""
    def __init__(self, diameter: Union[int, float], length: Union[int, float]):
        self._name = "Цилиндр"
        self._d = diameter
        self._l = length
        self._checkSizes()

    def _checkSizes(self):
        if self._d <= 0 or self._l <= 0:
            raise BodySizeException("размер не может быть отрицательным",
                                    self.__class__.__name__)

    def __repr__(self):
        return f"Тело '{self._name}':" \
               f"\n - диаметр d = {self._d}" \
               f"\n - длина l = {self._l}"

    def getSize(self) -> dict:
        return {'d': self._d, 'l': self._l}

    def getVolume(self) -> float:
        return 0.25 * pi * self._d**2 * self._l

    @property
    def diameter(self) -> float:
        return self._d

    @diameter.setter
    def diameter(self, diameter: float):
        if diameter > 0:
            self._d = diameter

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
    print(c.getSize())
