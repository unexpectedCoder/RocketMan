from typing import NoReturn, Union
import numpy as np

from ..exceptions.exception import SurfaceNameException
from .coordinate import Coordinate


class Velocity(Coordinate):
    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0, z: Union[int, float] = 0):
        Coordinate.__init__(self, x, y, z)
        self._update()

    def _update(self) -> NoReturn:
        Coordinate._update(self)
        xz = np.sqrt(self._xyz[0]**2 + self._xyz[2]**2)
        if self.x == 0 and self.y == 0 and self.z == 0:
            self.angle_to_xz = 0                            # Угол с горизонталью
            self.angle_to_xy = 0                            # Угол с вертикалью
        else:
            self.angle_to_xz = np.arctan(self._xyz[1] / xz)
            self.angle_to_xy = np.arctan(self._xyz[2] / self._xyz[0])
    
    def __repr__(self):
        return f"Вектор скорости:" \
               f"\n\t - компоненты: ({self._xyz[0]}; {self._xyz[1]}; {self._xyz[2]})" \
               f"\n\t - модуль: {self.getMagnitude()}" \
               f"\n\t - угол наклона к вертикали: {np.rad2deg(self.angle_to_xy)}" \
               f"\n\t - угол наклона к горизонту: {np.rad2deg(self.angle_to_xz)}"

    def __copy__(self):
        return Velocity(self._xyz[0], self._xyz[1], self._xyz[2])
    
    @classmethod
    def fromMagnitudeAndAngle(cls, mag: float, horiz_angle: float, vertic_angle: float, deg=True) -> 'Velocity':
        """Способ создания экземпляра. Углы отсчитываются против часовой стрелки.
        
        :param mag: длина (модуль) вектора скорости.
        :param horiz_angle: угол к горизонтальной плоскости.
        :param vertic_angle: угол к вертикальной плоскости.
        :param deg: флаг - в градусах (True) или радианах (False).
        """
        alpha = np.deg2rad(horiz_angle) if deg else horiz_angle
        beta = np.deg2rad(vertic_angle) if deg else vertic_angle
        xz = mag*np.cos(alpha)
        x = xz*np.cos(beta)
        y = mag*np.sin(alpha)
        z = xz*np.sin(beta)
        return Velocity(x, y, z)
    
    def getMagnitude(self) -> float:
        return np.sqrt(sum([val**2 for val in self._xyz]))
    
    def getAngle(self, to_surface: str, deg=False) -> float:
        try:
            angle = self._chooseAngle(to_surface)
            if deg:
                return np.rad2deg(angle)
            return angle
        except SurfaceNameException as ex:
            print(ex)

    def _chooseAngle(self, to_surface: str) -> float:
        if to_surface == 'xz':
            return self.angle_to_xz
        if to_surface == 'xy':
            return self.angle_to_xy
        raise SurfaceNameException(f"Параметр 'to_surface' не принимает значение {to_surface}!",
                                   src=self.__class__.__name__)
