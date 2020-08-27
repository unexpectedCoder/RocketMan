from scipy.interpolate import interp1d
from typing import NoReturn, Tuple, Union
import numpy as np

from core.exceptions import OutOfRangeException
from core.parsers import AtmosphereTxtFileParser
from core.types.atmosphere import Atmosphere


class TabularAtmosphere(Atmosphere):
    """Табулированная стандартная атмосфера."""

    def __init__(self, src_path: str, split='\t', with_head=True, standard='ГОСТ 4401-81'):
        self._standard = standard
        self._parser = AtmosphereTxtFileParser(src_path, split, with_head)
        self._hRange = self.determineHeightRange(self._parser.getHeightData())
        self._hData, self._TData, self._pData, self._rhoData = None, None, None, None
        self._TFunc, self._pFunc, self._rhoFunc = self._interpolateData()

    def __copy__(self):
        return TabularAtmosphere(self._parser.getSrcFilePath(),
                                 self._parser.getSplit(),
                                 self._parser.isWithHeader(),
                                 self._standard)

    def __repr__(self):
        return f" *** Стандартная атмосфера (по {self._standard}) ***" \
               f"\n\t - парсер: {self._parser}" \
               f"\n\t - диапазон высот: от {self._hRange[0]} до {self._hRange[1]}" \
               f"\n\t - функции температуры, давления и плотности табулированы по высоте"

    @staticmethod
    def determineHeightRange(height_data: np.ndarray) -> np.ndarray:
        return np.array((height_data[0], height_data[-1]))

    def _interpolateData(self) -> Tuple[interp1d, interp1d, interp1d]:
        self._hData, self._TData, self._pData, self._rhoData = self._parser.readSrcFile()
        return interp1d(self._hData, self._TData, kind='cubic'), \
               interp1d(self._hData, self._pData, kind='linear'), \
               interp1d(self._hData, self._rhoData, kind='linear')

    def getParser(self) -> AtmosphereTxtFileParser:
        """Используемый парсер source-файла."""
        return self._parser

    def getHeightRange(self) -> np.ndarray:
        """Диапазон высот."""
        return self._hRange

    def getHeight(self) -> np.ndarray:
        """Массив высоты."""
        return self._hData

    def getTemperature(self) -> np.ndarray:
        """Массивы температуры."""
        return self._TData

    def getPressure(self) -> np.ndarray:
        """Массив давления."""
        return self._pData

    def getDensity(self) -> np.ndarray:
        """Массив плотности."""
        return self._rhoData

    def T(self, h: Union[int, float, np.ndarray]) -> Union[float, np.ndarray]:
        """Интерполированное значение температуры."""
        self._checkHeightValue(h)
        return self._TFunc(h)

    def p(self, h: Union[int, float, np.ndarray]) -> Union[float, np.ndarray]:
        """Интерполированное значение давления."""
        self._checkHeightValue(h)
        return self._pFunc(h)

    def rho(self, h: Union[int, float, np.ndarray]) -> Union[float, np.ndarray]:
        """Интерполированное значение плотности."""
        self._checkHeightValue(h)
        return self._rhoFunc(h)

    def _checkHeightValue(self, h: Union[int, float, np.ndarray]) -> NoReturn:
        arrayCase = isinstance(h, np.ndarray) and not (self._hRange[0] <= any(h) <= self._hRange[1])
        floatCase = isinstance(h, float) and not (self._hRange[0] <= h <= self._hRange[1])
        intCase = isinstance(h, int) and not (self._hRange[0] <= h <= self._hRange[1])
        if arrayCase or floatCase or intCase:
            raise OutOfRangeException("Выход за границы интерполяции", src=self.__class__.__name__)

    def changeStandard(self, new_std: str) -> NoReturn:
        """Устанавливает новый стандарт атмосферы."""
        self._standard = new_std

    def getStandard(self) -> str:
        """Используемый стандарт параметров атмосферы."""
        return self._standard


# Test Drive
if __name__ == '__main__':
    from copy import copy

    atmos = TabularAtmosphere('../../tests/atmosphere_test.txt', split='\t')
    print(atmos)

    atmosOther = copy(atmos)
    atmosOther.changeStandard("АЗАЗА-4 миллиона")
    print(atmosOther)
    print(atmos)

    try:
        atmos.p(-1)
    except OutOfRangeException as ex:
        print(ex)
