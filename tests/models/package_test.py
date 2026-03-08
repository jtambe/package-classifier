import pytest
from pydantic import ValidationError

from models.package import Package

def test_negative_width():
    with pytest.raises(ValidationError):
        Package(width=-1.0, height=10.0, length=10.0, mass=10.0)

def test_negative_height():
    with pytest.raises(ValidationError):
        Package(width=10.0, height=-1.0, length=10.0, mass=10.0)

def test_negative_length():
    with pytest.raises(ValidationError):
        Package(width=10.0, height=10.0, length=-1.0, mass=10.0)

def test_negative_mass():
    with pytest.raises(ValidationError):
        Package(width=10.0, height=10.0, length=10.0, mass=-1.0)

def test_heavy_package():
    package = Package(width=10.0, height=10.0, length=10.0, mass=20.0)
    assert package.is_heavy == True

@pytest.mark.parametrize("width,height,length,mass", [
    (10.0, 10.0, 10.0, 19.99),
    (150.0, 10.0, 10.0, 10.0),
    (10.0, 150.0, 10.0, 10.0),
    (10.0, 10.0, 150.0, 10.0),
])
def test_not_heavy_package(width, height, length, mass):
    package = Package(width=width, height=height, length=length, mass=mass)
    assert package.is_heavy == False

@pytest.mark.parametrize("width,height,length,mass", [
    (150.0, 10.0, 10.0, 10.0),
    (10.0, 150.0, 10.0, 10.0),
    (10.0, 10.0, 150.0, 10.0),
])
def test_bulky_package_by_dimensions(width, height, length, mass):
    package = Package(width=width, height=height, length=length, mass=mass)
    assert package.is_bulky == True

@pytest.mark.parametrize("width,height,length,mass", [
    (100.0, 100.0, 100.0, 19.99),
])
def test_bulky_package_by_volume(width, height, length, mass):
    package = Package(width=width, height=height, length=length, mass=mass)
    assert package.is_bulky == True

