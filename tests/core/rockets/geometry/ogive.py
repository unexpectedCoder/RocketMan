from core.rockets.geometry.ogive import Ogive


def test_init_with_l():
    ogive = Ogive(.5, .4, arg_is='l')
    assert ogive.diameter == .5 and ogive.length == .4


def test_init_with_R():
    ogive = Ogive(.5, .4, arg_is='R')
    assert ogive.diameter == .5 and ogive.R == .4


def test_volume_R():
    ogive = Ogive(.5, .4, arg_is='R')
    assert round(ogive.volume, 10) == .0435441825
    ogive.R = 2.1
    assert round(ogive.volume, 10) != .0435441825
    ogive.R = .4
    assert round(ogive.volume, 10) == .0435441825


def test_volume_l():
    ogive = Ogive(.5, .4)
    assert round(ogive.volume, 10) == .0462950786
    ogive.diameter = 1.5
    assert round(ogive.volume, 10) != .0462950786
    ogive.diameter = .5
    assert round(ogive.volume, 10) == .0462950786
    ogive.length = 1.25
    assert round(ogive.volume, 10) != .0462950786
    ogive.length = .4
    assert round(ogive.volume, 10) == .0462950786


def test_drive():
    print()

    ogive = Ogive(.5, .4, arg_is='R')
    print(ogive)
    print(ogive.size)

    ogive = Ogive(.5, .4, arg_is='l')
    print(ogive)
    print(ogive.size)

    assert True
