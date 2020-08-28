from core.types.velocity import Velocity


def test_equal():
    v1 = Velocity(1, 0, -3)
    v2 = Velocity(1, 0, -3)
    v3 = Velocity()
    assert v1 == v2 and v2 != v3


def test_drive():
    print()
    print(Velocity(10, 5, 25))
    v = Velocity.fromMagnitudeAndAngle(1, 45, 0)
    print(f"В плоскости стрельбы под 45: {v}")
    v = Velocity.fromMagnitudeAndAngle(1, 135, 0)
    print(f"В плоскости стрельбы под 135: {v}")
    v = Velocity.fromMagnitudeAndAngle(1, -45, 0)
    print(f"В плоскости стрельбы под -45: {v}")
    v = Velocity.fromMagnitudeAndAngle(1, 315, 0)
    print(f"В плоскости стрельбы под 315: {v}")
    v = Velocity.fromMagnitudeAndAngle(1, 225, 0)
    print(f"В плоскости стрельбы под 225: {v}")
    v = Velocity.fromMagnitudeAndAngle(1, 45, 45)
    print(f"Общий случай 45 и 45: {v}")
    v = Velocity.fromMagnitudeAndAngle(1, 45, 135)
    print(f"Общий случай 45 и 135: {v}")
    v = Velocity.fromMagnitudeAndAngle(1, 210, 0)
    print(f"В плоскости стрельбы под 210: {v}")
    assert True
