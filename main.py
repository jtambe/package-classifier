from models.package import Package

def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Sort the package based on its dimensions and mass.
    """    
    package = Package(width=width, height=height, length=length, mass=mass)
    classification = package.sort()
    return str(classification.name)