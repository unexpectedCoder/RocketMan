from src.geometry.body import Body
from src.core.errors import BodySizeError

from math import pi


class Sphere(Body):
    """Сфера (полная и сегмент)."""
    type = 'sphere'

    def __init__(self, size: dict):
        Body.__init__(self, size)
        self._check_size()

    def _check_size(self):
        keys = self.size.keys()
        if 'd' not in keys:
            raise BodySizeError("Неправильные ключи переданного словаря размера! " \
                                "Должны быть ключи 'd' (диаметр) (опционально - 'h' (высота сектора))...", self.__class__)
        if 'h' not in keys or self.size['h'] > self.size['d']:
            self.size['h'] = self.size['d']                         # Случай полной сферы

    def get_volume(self) -> float:
        return pi * self.size['h']**2 * (0.5*self.size['d'] - self.size['h'] / 3)

    @property
    def diameter(self) -> float:
        return self.size['d']

    @diameter.setter
    def diameter(self, d: float):
        if d > 0:
            self.size['d'] = d

    @property
    def sector_height(self) -> float:
        return self.size['h']

    @sector_height.setter
    def sector_height(self, h: float):
        if h > 0:
            self.size['h'] = h
