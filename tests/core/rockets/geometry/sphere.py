from core.exceptions.exception import BodySizeException
from core.rockets.geometry.sphere import Sphere


def test_correct_init():
    try:
        Sphere(10, 20)
        Sphere(10)
        assert True
    except BodySizeException:
        assert False


def test_incorrect_init():
    try:
        Sphere(-10)
        assert False
    except BodySizeException:
        assert True


def test_size():
    assert Sphere(10.5, .25).size == {'d': 10.5, 'h': .25}


def test_full_volume():
    assert round(Sphere(5.2).volume, 10) == 73.6221766393


def test_segment_volume():
    assert round(Sphere(5.2, 1.5).volume, 10) == 14.8440252882


def test_diameter_property():
    s = Sphere(5., 2.)
    assert s.diameter == 5
    s.diameter = 10.5
    assert s.diameter == 10.5


def test_height_property():
    s = Sphere(5., 2.)
    assert s.segmentHeight == 2.
    s.segmentHeight = 1.2
    assert s.segmentHeight == 1.2
    s = Sphere(5.)
    assert s.segmentHeight == 5
    s.segmentHeight = 200
    assert s.segmentHeight == 5
