from abc import ABC, abstractmethod


class Visualizer(ABC):
    """Интерфейс визуализатора данных и объектов."""

    @abstractmethod
    def display(self):
        """Выводит графическую информацию об объекте."""
        pass

