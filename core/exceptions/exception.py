from .custom_exception import CustomException


class OutOfRangeException(CustomException):
    """Ислючение в случае выхода значения переменной за допустимые границы."""
    pass


class SurfaceNameException(CustomException):
    """Исключение в случае использования несуществующего имени поверхности."""
    pass