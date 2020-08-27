from typing import NoReturn, Union
import numpy as np


class Coordinate:
    """Пространственная координата (точка).

    Координатная система по умолчанию:
    - ось :math:`0x` -- по направлению на цель;
    - ось :math:`0y` -- вертикально вверх (по нормали к поверхности);
    - ось :math:`0z` -- в боковом направлении (правая тройка векторов).
    """
    
    def __init__(self, x: Union[int, float] = 0, y: Union[int, float] = 0, z: Union[int, float] = 0):
        self._xyz = np.array([x, y, z])

    def __eq__(self, other):
        for a, b in zip(self.xyz, other.xyz):
            if a != b:
                return False
        return True

    def __repr__(self):
        return f"Координата: ({self._xyz[0]}; {self._xyz[1]}; {self._xyz[2]})"

    def __copy__(self):
        return Coordinate(self._xyz[0], self._xyz[1], self._xyz[2])
    
    @property
    def xyz(self) -> np.ndarray:
        """Текущее значение координаты."""
        return self._xyz

    @xyz.setter
    def xyz(self, new_xyz: Union[list, tuple, np.ndarray]) -> NoReturn:
        """Задать новое значение координаты."""
        self._xyz = np.array(new_xyz) if not isinstance(new_xyz, np.ndarray) else new_xyz.copy()
        self._update()

    def _update(self):
        self.x, self.y, self.z = self._xyz.tolist()

    def getX(self) -> float:
        """X-составляющая координаты."""
        return self._xyz[0]

    def getY(self) -> float:
        """Y-составляющая координаты."""
        return self._xyz[1]

    def getZ(self) -> float:
        """Z-составляющая координаты."""
        return self._xyz[2]


# Test Drive
if __name__ == '__main__':
    print(Coordinate(1.5, 0.5, -3))
