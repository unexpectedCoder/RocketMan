from numpy import pi, sqrt, arcsin
from typing import Union

from core.exceptions.exception import OgiveSizeException
from .geometry import Geometry


class Ogive(Geometry):
    """Геометрия оживала."""

    def __init__(self, d: Union[int, float], length: Union[int, float]):
        self.checkSize(d, length)
        if d == 0:
            raise OgiveSizeException("диаметр оживала не может быть нулевым",
                                     src=self.__class__.__name__)
        self._name = "Оживало"
        self._d, self._l = d, length

    def __repr__(self):
        return f"Тело '{self._name}'" \
               f"\n - диаметр d = {self._d}" \
               f"\n - длина l = {self._l}" \
               f"\n - объем V = {self.volume}"

    @property
    def size(self) -> dict:
        return {'d': self._d, 'l': self._l, 'volume': self.volume}

    @property
    def volume(self) -> float:
        r = 0.5*self._d
        l = self._l
        R = (r + l)**2 / (2*r) - l
        if l > r:
            raise OgiveSizeException("длина оживала не должна превышать его радиус",
                                     src=self.__class__.__name__)
        return pi*(l*(R**2 - l**2 / 3) + R**2 * sqrt(R**2 - l**2) * arcsin(l/R))

    @property
    def diameter(self) -> float:
        return self._d

    @diameter.setter
    def diameter(self, d: Union[int, float]):
        if d > 0:
            self._d = d

    @property
    def length(self) -> float:
        return self._l

    @length.setter
    def length(self, l: Union[int, float]):
        if l > 0:
            self._l = l


# Test Drive
# if __name__ == '__main__':
#     size = {'d': 100, 'r': 200}
#     ogive = Ogive(size)
#     print(ogive.get_size())
#     print(ogive.get_volume())
