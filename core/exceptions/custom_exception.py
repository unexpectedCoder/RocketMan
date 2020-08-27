from abc import ABC


class CustomException(ABC, Exception):
    def __init__(self, txt: str, src=None):
        Exception.__init__(self)
        txt = txt.lower()
        self._txt = f"ИСКЛЮЧЕНИЕ <{self.__class__.__name__}> брошено из объекта <{src}>: {txt}!" if src \
            else f"ИСКЛЮЧЕНИЕ <{self.__class__.__name__}>: {txt}!"

    def __str__(self):
        return self._txt
