from numpy import array

from core.types.coordinate import Coordinate


def test_default_init():
    coord = Coordinate()
    assert any(coord.xyz == array([0, 0, 0]))


def test_partial_init():
    coord = Coordinate(y=-1)
    assert any(coord.xyz == array([0, -1, 0]))


def test_full_init():
    coord = Coordinate(-1.5, 2, 3.)
    assert any(coord.xyz == array([-1.5, 2, 3.]))


def test_reset_xyz():
    coord = Coordinate(1, 2, 3)
    assert any(coord.xyz == array([1, 2, 3]))
    coord.xyz = 1, 0.5, -1
    assert any(coord.xyz == array([1, 0.5, -1]))


def test_copy():
    from copy import copy
    c1 = Coordinate()
    c2 = copy(c1)
    c2.xyz = 1, 0, -1
    assert any(c1.xyz == array([0, 0, 0])) and any(c2.xyz == array([1, 0, -1]))


def test_equal():
    c1 = Coordinate(-1, 1.5, 0.25)
    c2 = Coordinate(-1, 1.5, 0.25)
    c3 = Coordinate()
    assert c1 == c2 and c2 != c3
