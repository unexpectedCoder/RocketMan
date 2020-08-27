from core.types.velocity import Velocity


def test_equal():
    v1 = Velocity(1, 0, -3)
    v2 = Velocity(1, 0, -3)
    v3 = Velocity()
    assert v1 == v2 and v2 != v3
