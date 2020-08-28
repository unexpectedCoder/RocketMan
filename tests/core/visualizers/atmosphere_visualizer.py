from core.types.tabular_atmosphere import TabularAtmosphere
from core.visualizers import AtmosphereVisualizer


def test_drive():
    vis = AtmosphereVisualizer(TabularAtmosphere('atmosphere_test.txt'))
    vis.display()
    assert True
