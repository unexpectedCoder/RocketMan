from abc import ABC, abstractmethod


class Rocket(ABC):
    """Абстрактный класс ракеты."""
    def __init__(self,
                 construction,
                 cargo,
                 control_sys,
                 engine):
        pass
