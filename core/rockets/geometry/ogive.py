# import numpy as np
#
# from .geometry import Geometry
# from core.exceptions.exception import BodySizeException
#
#
# class Ogive(Geometry):
#     """Оживало (полное и усеченное)."""
#     type = 'ogive'
#
#     def __init__(self, size: dict):
#         Body.__init__(self, size)
#
#     def _check_size(self):
#         keys = self.size.keys()
#         if 'd' not in keys or 'r' not in keys:
#             raise BodySizeError("Неправильные ключи переданного словаря размера! " \
#                                 "Должны быть ключи 'd' (диаметр корпуса) и 'r' (радиус оживала) " \
#                                 "('a' - опционально - доля участка оживала до урезанного участка) от 0 до 1...",
#                                 self.__class__)
#         if 'a' not in keys:
#             self.size['a'] = 1
#         if self.size['a'] < 0:
#             self.size['a'] = 0
#         elif self.size['a'] > 1:
#             self._check_size['a'] = 1
#
#     def get_volume(self) -> float:
#         """Объём оживала."""
#         nr, nalpha = 500, 500
#         dr = self._calc_long_step(0., 0.5*self.size['d'], nr)
#         radiuses = np.linspace(0, 0.5*self.size['d'], dr)
#         dalpha = self._calc_trans_step(nalpha)
#         return np.sum(self._calc_trans_square(radiuses, dalpha)) * nalpha
#
#     def _calc_long_step(self, x1: float, x2: float, n: int) -> float:
#         # Рассчитать шаг по продольному сечению
#         if n == 0:
#             raise ValueError(f"Ошибка в {self.__class__}: кол-во разбиений должно быть > 0!")
#         x1 = self._ogive_equation(0.)
#         x2 = self._ogive_equation(0.5*self.size['d'])
#         return abs(x2 - x1) / n
#
#     def _ogive_equation(self, x: float) -> float:
#         return np.sqrt(self.size['r']**2 - (x + self.size['r'] - 0.5*self.size['d'])**2)
#
#     def _calc_trans_step(self, n: int) -> float:
#         # Рассчитать шаг в попереном сечении
#         if n == 0:
#             raise ValueError(f"Ошибка в {self.__class__}: кол-во разбиений должно быть > 0!")
#         return 2 * np.pi / n
#
#     def _calc_trans_square(self, r: np.ndarray, dalpha: float) -> np.ndarray:
#         # Площадь сегмента поперечного сечения
#         return 0.5 * r**2 * dalpha
#
#
# # Тест
# if __name__ == '__main__':
#     size = {'d': 100, 'r': 200}
#     ogive = Ogive(size)
#     print(ogive.get_size())
#     print(ogive.get_volume())
