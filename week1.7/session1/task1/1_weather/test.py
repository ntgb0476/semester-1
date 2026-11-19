from weather import comfort_level


def test_cold():
    assert comfort_level(5) == "COLD"
    assert comfort_level(200) == "COLD"


test_cold()
