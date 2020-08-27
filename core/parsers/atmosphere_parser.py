from os import path
from typing import Iterator, Iterable, List, Tuple
import numpy as np


class AtmosphereTxtFileParser:
    def __init__(self, src_path: str, split='\t', with_head=True):
        self._srcPath = src_path
        self._split = split
        self._header = self._readSrcFileHeader() if with_head else ""
        self._withHeader = with_head
        self._isRead = False

    def _readSrcFileHeader(self) -> List[str]:
        with open(self._srcPath, 'r') as file:
            return next(iter(file)).strip().split(self._split)

    def getHeightData(self) -> np.ndarray:
        """Массив значений высот из source-файла."""
        with open(self._srcPath, 'r') as file:
            line = self._withoutHeader(file)
            try:
                h = []
                while True:
                    h.append(float(next(line).split(self._split)[0]))
            except StopIteration:
                pass
            finally:
                return np.array(h)

    def readSrcFile(self) -> Tuple[np.ndarray, ...]:
        h, temp, p, rho = [], [], [], []
        with open(self._srcPath, 'r') as file:
            line = self._withoutHeader(file)
            try:
                while True:
                    buf = [float(value) for value in next(line).split(self._split)]
                    h.append(buf[0])
                    temp.append(buf[1])
                    p.append(buf[2] * 1e5)
                    rho.append(buf[3])
            except StopIteration:
                self._isRead = True
                return np.array(h), np.array(temp), np.array(p), np.array(rho)

    def _withoutHeader(self, file: Iterable) -> Iterator:
        line = iter(file)
        if self._header != "":
            next(line)
        return line

    def getSrcFilePath(self) -> str:
        return path.abspath(self._srcPath)

    def getSplit(self) -> str:
        return self._split

    def isWithHeader(self) -> bool:
        return self._withHeader
