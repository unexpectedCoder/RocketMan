from abc import ABC, abstractmethod

# from core.exceptions.exception import BodySizeException


class Geometry(ABC):
    """Абстрактный класс геометрии."""
    _name = None
    _size = None

    # def __init__(self,):
    #     self._name = "NO NAME"
    #     self._size = None

    # def _checkSizeForNegative(self):
    #     for key in self._size.keys():
    #         if self._size[key] < 0:
    #             raise BodySizeException("Что-то не так с геометрическими размерами тела - "
    #                                     "они должны быть неотрицательными!",
    #                                     src=self.__class__.__name__)

    def __repr__(self):
        s = self._name
        for key in self._size.keys():
            s += f"\n\t {key} = {self._size[key]} [мм]"

    def getName(self) -> str:
        """Название тела."""
        return self._name

    @abstractmethod
    def getSize(self) -> dict:
        """Размеры тела."""
        pass

    @abstractmethod
    def getVolume(self) -> float:
        """Объём тела."""
        pass
