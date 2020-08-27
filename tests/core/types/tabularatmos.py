from core.types.tabularatmos import TabularAtmosphere


def test_temperature():
    atmo = TabularAtmosphere('../../atmosphere_test.txt', split='\t')
    assert atmo.T(0.) == 290. and atmo.T(500.) == 320.


def test_pressure():
    atmo = TabularAtmosphere('../../atmosphere_test.txt', split='\t')
    assert atmo.p(0.) == 1.01e5 and atmo.p(100.) == 1e5


def test_density():
    atmo = TabularAtmosphere('../../atmosphere_test.txt', split='\t')
    assert atmo.rho(100.) == 1.2 and atmo.rho(800.) == 1.


def test_invalid_height():
    from core.exceptions import OutOfRangeException

    atmo = TabularAtmosphere('../../atmosphere_test.txt', split='\t')
    try:
        atmo.p(-1000)
        assert False
    except OutOfRangeException:
        assert True
