from core.rockets.geometry.cylinder import Cylinder
from core.exceptions.exception import BodySizeException


def test_invalid_init():
    try:
        Cylinder(-3, 2)
        assert False
    except BodySizeException:
        assert True


def test_get_size():
    size = Cylinder(0.5, 1.75).getSize()
    assert size == {'d': 0.5, 'l': 1.75}


def test_diameter_property():
    c = Cylinder(10, 20.5)
    assert c.diameter == 10
    c.diameter = 0.5
    assert c.diameter == 0.5


def test_length_property():
    c = Cylinder(10, 20.5)
    assert c.length == 20.5
    c.length = 5
    assert c.length == 5
