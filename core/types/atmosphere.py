from abc import ABC, abstractmethod
from typing import Union
from numpy import ndarray


class Atmosphere(ABC):
    """Интерфейс атмосферы."""
    @abstractmethod
    def getHeightRange(self) -> ndarray:
        pass

    @abstractmethod
    def getHeight(self) -> ndarray:
        pass

    @abstractmethod
    def getTemperature(self) -> ndarray:
        pass

    @abstractmethod
    def getPressure(self) -> ndarray:
        pass

    @abstractmethod
    def getDensity(self) -> ndarray:
        pass

    @abstractmethod
    def T(self, h: Union[float, ndarray]) -> Union[float, ndarray]:
        pass

    @abstractmethod
    def p(self, h: Union[float, ndarray]) -> Union[float, ndarray]:
        pass

    @abstractmethod
    def rho(self, h: Union[float, ndarray]) -> Union[float, ndarray]:
        pass
