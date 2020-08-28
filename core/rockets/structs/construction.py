from abc import ABC
from copy import copy


class Construction(ABC):
    def __init__(self, compartments):
        self.compartments = copy(compartments)
