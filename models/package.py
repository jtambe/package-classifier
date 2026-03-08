from pydantic import BaseModel, ValidationError, field_validator, Field
from .package_classifications import PackageClassification

HEAVY_MASS = 20.0
BULKY_DIMENSION = 150.0
BULKY_VOLUME = 1000000.0

class Package(BaseModel):
    # reasonable assumptions made for the dimensions and mass of the package:
    width: float = Field(gt=0.0, le=10000)
    height: float = Field(gt=0.0, le=10000)
    length: float = Field(gt=0.0, le=10000)
    mass: float = Field(gt=0.0, le=1000)

    # @field_validator('width', 'height', 'length', 'mass')
    # @classmethod
    # def validate_positive(cls, v, info):
    #     if v < 0:
    #         raise ValueError(f'Invalid dimension: {info.field_name} must be non-negative')
    #     return v

    @property
    def is_heavy(self) -> bool:
        return self.mass >= HEAVY_MASS

    @property
    def is_bulky(self) -> bool:
        return (
            self.width >= BULKY_DIMENSION 
            or self.height >= BULKY_DIMENSION 
            or self.length >= BULKY_DIMENSION
            or self.width * self.height * self.length >= BULKY_VOLUME
        )
                    
    def sort(self) -> PackageClassification:
        heavy = self.is_heavy
        bulky = self.is_bulky

        if heavy and bulky:
            return PackageClassification.REJECTED
        if heavy or bulky:
            return PackageClassification.SPECIAL
        return PackageClassification.STANDARD


        