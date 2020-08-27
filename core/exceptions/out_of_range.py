class OutOfRangeException(Exception):
    def __init__(self, txt: str, src=None):
        txt = txt.lower()
        self._txt = f"ИСКЛЮЧЕНИЕ брошено из объекта <{src}>: {txt}!" if src else f"ИСКЛЮЧЕНИЕ: {txt}!"

    def __str__(self):
        return self._txt
