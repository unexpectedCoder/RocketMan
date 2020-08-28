from abc import ABC, abstractproperty

from core.exceptions.exception import BodySizeException


class Geometry(ABC):
    """Абстрактный класс геометрии."""
    _name = None
    _size = None

    def checkSize(self, *args):
        for arg in args:
            if arg < 0:
                raise BodySizeException("размер не может быть отрицательным",
                                        src=self.__class__.__name__)

    def __repr__(self):
        s = self._name
        for key in self._size.keys():
            s += f"\n\t {key} = {self._size[key]} [мм]"

    @property
    def getName(self) -> str:
        """Название тела."""
        return self._name

    @abstractproperty
    def size(self) -> dict:
        """Размеры тела."""
        pass

    @abstractproperty
    def volume(self) -> float:
        """Объём тела."""
        pass
