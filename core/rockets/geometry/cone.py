from src.geometry.body import Body
from src.core.errors import BodySizeError

from math import pi


class Cone(Body):
    """Конус (полный и усеченный)."""
    type = 'cone'

    def __init__(self, size: dict):
        Body.__init__(self, size)
        self._check_size()

    def _check_size(self):
        if self.size['d1'] > self.size['d2']:
            self.size['d1'], self.size['d2'] = self.size['d2'], self.size['d1']
        keys = self.size.keys()
        if 'd1' not in keys or 'd2' not in keys or 'h' not in keys:
            raise BodySizeError("Неправильные ключи переданного словаря размера! " \
                                "Должны быть ключи 'd1', 'd2' (диаметры оснований) и 'h' (высота)...", self.__class__)

    def get_volume(self) -> float:
        return 1/12*pi*self.size['h']*(self.size['d1']**2 + self.size['d2']**2 + self.size['d1']*self.size['d2'])

    @property
    def diameter_smaller(self) -> float:
        return self.size['d1']

    @diameter_smaller.setter
    def diameter_smaller(self, d: float):
        if d > 0:
            self.size['d1'] = d

    @property
    def diameter_larger(self) -> float:
        return self.size['d2']

    @diameter_larger.setter
    def diameter_larger(self, d: float):
        if d > 0:
            self.size['d2'] = d

    @property
    def height(self) -> float:
        return self.size['h']

    @height.setter
    def height(self, h: float):
        if h > 0:
            self.size['h'] = h
