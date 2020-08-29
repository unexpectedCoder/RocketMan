from numpy import pi, sqrt, arcsin
from typing import Union

from core.exceptions.exception import OgiveSizeException, InvalidConstructArgumentException
from .geometry import Geometry


class Ogive(Geometry):
    """Геометрия оживала."""

    def __init__(self, d: Union[int, float], arg: Union[int, float], arg_is: str = 'l'):
        self.checkSize(d, arg)
        if d == 0:
            raise OgiveSizeException("диаметр оживала не может быть нулевым",
                                     src=self.__class__.__name__)
        self._name = "Оживало"
        self._d = d
        self._arg, self._argIs = arg, arg_is
        self._update()

    def _update(self):
        if self._argIs == 'l':
            self._l = self._arg
            self._R = self._calcR(0.5*self._d, self._l)
        elif self._argIs == 'R':
            self._R = self._arg
            self._l = self._calcLength(0.5*self._d, self._R)
        else:
            raise InvalidConstructArgumentException(f"нет возможности расчета оживала по размеру {self._argIs}",
                                                    src=self.__class__.__name__)

    def _calcR(self, r: Union[int, float], l: Union[int, float]) -> float:
        if (r + l)**2 / (2*r) - l < 0:
            raise OgiveSizeException(f"слишком большая длина оживала l={l}",
                                     src=self.__class__.__name__)
        return (r + l)**2 / (2*r) - l

    def _calcLength(self, r: Union[int, float], R: Union[int, float]) -> float:
        if r > R:
            raise OgiveSizeException(f"радиус основания r={r} должен быть меньше радиуса оживала R={R}",
                                     src=self.__class__.__name__)
        return sqrt(2*r*R - r**2)

    def __repr__(self):
        return f"Тело '{self._name}'" \
               f"\n - диаметр основания d = {self._d}" \
               f"\n - длина l = {self._l}" \
               f"\n - радиус оживала R = {self._R}" \
               f"\n - объем V = {self.volume}"

    @property
    def size(self) -> dict:
        return {'d': self._d, 'l': self._l, 'R': self._R}

    @property
    def volume(self) -> float:
        l = self._l
        R = self._R
        if l > R:
            raise OgiveSizeException("длина оживала не должна превышать его радиус",
                                     src=self.__class__.__name__)
        return pi*(l*(R**2 - l**2 / 3) - R**2 * sqrt(R**2 - l**2) * arcsin(l/R))

    @property
    def diameter(self) -> float:
        return self._d

    @diameter.setter
    def diameter(self, d: Union[int, float]):
        if d > 0:
            self._d = d
            self._update()

    @property
    def length(self) -> float:
        return self._l

    @length.setter
    def length(self, l: Union[int, float]):
        if l > 0:
            self._argIs, self._arg = 'l', l
            self._update()

    @property
    def R(self) -> float:
        return self._R

    @R.setter
    def R(self, new_r: Union[int, float]):
        if new_r > 0:
            self._argIs, self._arg = 'R', new_r
            self._update()
