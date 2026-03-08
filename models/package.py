from pydantic import BaseModel, Field
from .package_classifications import PackageClassification

HEAVY_MASS = 20.0
BULKY_DIMENSION = 150.0
BULKY_VOLUME = 1000000.0

class Package(BaseModel):
    """
    Defines the Package model with validation for dimensions and mass. 
    The following are the reasonable assumptions made for the dimensions and mass of the package:
    - width, height, length: greater than 0.0 and less than or equal to 10,000.0 cm
    - mass: greater than 0.0 and less than or equal to 1,000.0 kg
    """
    width: float = Field(gt=0.0, le=10000)
    height: float = Field(gt=0.0, le=10000)
    length: float = Field(gt=0.0, le=10000)
    mass: float = Field(gt=0.0, le=1000)

    @property
    def is_heavy(self) -> bool:
        """
        A package is considered heavy if its mass is greater than or equal to 20 kg.
        """
        return self.mass >= HEAVY_MASS

    @property
    def is_bulky(self) -> bool:
        """
        A package is considered bulky if any of its dimensions are greater than or equal to 150 cm, 
        or if its volume is greater than or equal to 1,000,000 cm³.
        """
        return (
            self.width >= BULKY_DIMENSION 
            or self.height >= BULKY_DIMENSION 
            or self.length >= BULKY_DIMENSION
            or self.width * self.height * self.length >= BULKY_VOLUME
        )
                    
    def sort(self) -> PackageClassification:
        """
        Classify the package based on its dimensions and mass.
        """
        heavy = self.is_heavy
        bulky = self.is_bulky

        if heavy and bulky:
            return PackageClassification.REJECTED
        if heavy or bulky:
            return PackageClassification.SPECIAL
        return PackageClassification.STANDARD


        