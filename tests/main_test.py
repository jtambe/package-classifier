import pytest
from pydantic import ValidationError
from main import sort


@pytest.mark.parametrize("width,height,length,mass,expected", [
    (10.0, 10.0, 10.0, 10.0, "STANDARD"),
    (100.0, 100.0, 99.99, 19.99, "STANDARD"),
])
def test_sort_standard(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected


@pytest.mark.parametrize("width,height,length,mass,expected", [
    (150.0, 10.0, 10.0, 10.0, "SPECIAL"),
    (10.0, 150.0, 10.0, 10.0, "SPECIAL"),
    (10.0, 10.0, 150.0, 10.0, "SPECIAL"),
    (100.0, 10.0, 100.0, 20.0, "SPECIAL"),
])
def test_sort_special(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected


@pytest.mark.parametrize("width,height,length,mass,expected", [
    (150.0, 150.0, 150.0, 20.0, "REJECTED"),
    (150.0, 10.0, 10.0, 20.0, "REJECTED"),
    (10.0, 150.0, 10.0, 20.0, "REJECTED"),
    (10.0, 10.0, 150.0, 20.0, "REJECTED"),
    (100.0, 100.0, 100.0, 20.0, "REJECTED"),
])
def test_sort_rejected(width, height, length, mass, expected):
    assert sort(width, height, length, mass) == expected


@pytest.mark.parametrize("width,height,length,mass", [
    (100000000.0, 150.0, 150.0, 20.0),
    (150.0, 100000000.0, 10.0, 20.0),
    (10.0, 150.0, 100000000.0, 20.0),
    (10.0, 10.0, 150.0, 100000000.0),
    (0.0, 150.0, 150.0, 20.0),
    (150.0, 0.0, 10.0, 20.0),
    (10.0, 150.0, 0.0, 20.0),
    (10.0, 150.0, 150.0, 0.0),
    (-1.0, 150.0, 150.0, 20.0),
    (150.0, -1.0, 10.0, 20.0),
    (10.0, 150.0, -1.0, 20.0),
    (10.0, 150.0, 150.0, -1.0),
])
def test_sort_invalid(width, height, length, mass):
    with pytest.raises(ValidationError):
        sort(width, height, length, mass)