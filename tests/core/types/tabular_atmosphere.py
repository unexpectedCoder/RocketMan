from core.types.tabular_atmosphere import TabularAtmosphere


def test_temperature():
    atmo = TabularAtmosphere('atmosphere_test.txt', split='\t')
    assert atmo.T(0.) == 290. and atmo.T(500.) == 320.


def test_pressure():
    atmo = TabularAtmosphere('atmosphere_test.txt', split='\t')
    assert atmo.p(0.) == 1.01e5 and atmo.p(100.) == 1e5


def test_density():
    atmo = TabularAtmosphere('atmosphere_test.txt', split='\t')
    assert atmo.rho(100.) == 1.2 and atmo.rho(800.) == 1.


def test_invalid_height():
    from core.exceptions import OutOfRangeException

    atmo = TabularAtmosphere('atmosphere_test.txt', split='\t')
    try:
        atmo.p(-1000)
        assert False
    except OutOfRangeException:
        assert True


def test_using_array():
    from numpy import array

    h = array([0, 100, 500, 800])
    atmo = TabularAtmosphere('atmosphere_test.txt', split='\t')
    temp = atmo.T(h)
    if any(temp == [290., 300., 320., 340.]) is True:
        assert True
    else:
        assert False


def test_drive():
    from copy import copy
    from core.exceptions.exception import OutOfRangeException

    print()

    atmos = TabularAtmosphere('atmosphere_test.txt', split='\t')
    print(atmos)

    atmosOther = copy(atmos)
    atmosOther.changeStandard("АЗАЗА-4 миллиона")
    print(atmosOther)
    print(atmos)

    try:
        atmos.p(-1)
    except OutOfRangeException as ex:
        print(ex)

    assert True
