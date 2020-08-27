from copy import copy
from typing import Tuple, Union
import matplotlib.pyplot as plt
import numpy as np

from core.visualizers.visualizer import Visualizer
from core.types.atmosphere import Atmosphere


class AtmosphereVisualizer(Visualizer):
    """Визуализатор параметров атмосферы."""

    def __init__(self, atmos: Atmosphere, points=500):
        self._atmos = copy(atmos)
        self._points = points if points > 0 else 500        # Кол-во точек разбиения оси абсцисс
        self._h0 = self._atmos.getHeightRange()[0]

    def _calcHeightStep(self) -> float:
        hRange = self._atmos.getHeightRange()
        return (hRange[1] - hRange[0]) / self._points

    def display(self):
        """Выводит графики T(h), p(h) и rho(h)."""
        hTab, tTab, pTab, rhoTab = self._prepareTabularData()
        h, t, p, rho = self._prepareInterpolatedData()

        plt.figure("Параметры атмосферы", figsize=(12, 7))
        self.draw('311', (h, hTab), (t, tTab), '$h$ [м]', '$T$, [К]')
        self.draw('312', (h, hTab), (p*1e-6, pTab*1e-6), '$h$ [м]', r'$p$, [МПа]')
        self.draw('313', (h, hTab), (rho, rhoTab), '$h$ [м]', r'$\rho$, [кг/м$^3$]')
        plt.show()

    def _prepareTabularData(self) -> Tuple[np.ndarray, ...]:
        return self._atmos.getHeight(), \
               self._atmos.getTemperature(), \
               self._atmos.getPressure(), \
               self._atmos.getDensity()

    def _prepareInterpolatedData(self) -> Tuple[np.ndarray, ...]:
        hRange = self._atmos.getHeightRange()
        h = np.linspace(hRange[0], hRange[1], self._points + 1)
        t = self._atmos.T(h)
        p = self._atmos.p(h)
        rho = self._atmos.rho(h)
        return h, t, p, rho

    @staticmethod
    def draw(pos: str, xdata: Union[tuple, list, np.ndarray], ydata: Union[tuple, list, np.ndarray],
             xlabel: str, ylabel: str, title: str = '', grid=True):
        plt.subplot(pos)
        plt.plot(xdata[0], ydata[0])
        plt.plot(xdata[1], ydata[1], color='r', marker='x', ls='')
        plt.xlabel(xlabel)
        plt.ylabel(ylabel)
        plt.title(title)
        plt.grid(grid)


# Test Drive
if __name__ == '__main__':
    from core.types.tabular_atmosphere import TabularAtmosphere
    vis = AtmosphereVisualizer(TabularAtmosphere('../../tests/atmosphere_test.txt'))
    vis.display()
