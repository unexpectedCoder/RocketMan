from core.exceptions.exception import BodySizeException
from core.rockets.geometry.cone import Cone


def test_init_with_zero_d1():
    try:
        Cone(0, 50, 100)
        assert True
    except BodySizeException:
        assert False


def test_incorrect_init():
    try:
        Cone(0, -.1, 2)
        assert False
    except BodySizeException:
        assert True


def test_size():
    assert Cone(1.5, 2, 3.15).size == {'d1': 1.5, 'd2': 2, 'h': 3.15}


def test_full_volume():
    assert round(Cone(0, 1, 2).volume, 10) == .5235987756


def test_partial_volume():
    assert round(Cone(2, 3, 3.15).volume, 10) == 15.6686933598


def test_d1_property():
    c = Cone(1, 2.5, 3)
    assert c.diameterOne == 1
    c.diameterOne = .25
    assert c.diameterOne == .25


def test_d2_property():
    c = Cone(0, 2, 7)
    assert c.diameterTwo == 2
    c.diameterTwo = 1.5
    assert c.diameterTwo == 1.5


def test_height_property():
    c = Cone(1, 2, 3.1)
    assert c.height == 3.1
    c.height = 10
    assert c.height == 10


def test_repr():
    c = Cone(1.5, 2, 3.15)
    print()
    print(c)
    print(c.size)
    assert True
