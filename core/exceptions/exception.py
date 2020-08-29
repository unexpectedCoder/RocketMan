from .custom_exception import CustomException


class OutOfRangeException(CustomException):
    """Ислючение в случае выхода значения переменной за допустимые границы."""
    pass


class SurfaceNameException(CustomException):
    """Исключение в случае использования несуществующего имени поверхности."""
    pass


class BodySizeException(CustomException):
    """Исключение в случае некорректного размера тела."""
    pass


class OgiveSizeException(CustomException):
    """Исключение в случае некорректного размера оживала."""
    pass


class InvalidConstructArgumentException(CustomException):
    """Исключение в случае некоррекного аргумента в конструкторе класса."""
    pass
