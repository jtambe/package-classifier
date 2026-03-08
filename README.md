# Package Classifier

A Python package classification system that categorizes packages based on their dimensions and mass. Built with an object-oriented approach using Pydantic for validation and pytest for comprehensive unit testing.

## Features

- **Object-Oriented Design**: Clean separation of concerns with dedicated models and enums
- **Pydantic Validation**: Robust input validation with field constraints (ranges, type checking)
- **Comprehensive Testing**: Full test coverage using pytest with parameterized tests
- **Classification Logic**: Automatically classifies packages as STANDARD, SPECIAL, or REJECTED based on:
  - Mass threshold: 20.0 kg (heavy)
  - Dimension threshold: 150.0 cm (bulky)
  - Volume threshold: 1,000,000 cm³ (bulky)

## Project Structure

```
package-classifier/
├── models/
│   ├── __init__.py
│   ├── package.py                 # Package model with classification logic
│   └── package_classifications.py # Enum for package classifications
├── tests/
│   ├── main_test.py              # Integration tests
│   └── models/
│       └── package_test.py       # Unit tests for Package model
├── main.py                        # Driver function
├── requirements.txt               # Project dependencies
└── README.md
```

## Setup Instructions

### 1) Clone the repository

```bash
git clone https://github.com/jtambe/package-classifier.git
cd package-classifier
```

### 2) Create and activate a Python virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Install dependencies

Option 1 - Using requirements.txt:

```bash
pip install -r requirements.txt
```

Option 2 - Install packages directly:

```bash
pip install pydantic pytest
```

### 4) Run the tests

```bash
python -m pytest tests/
```

Or for verbose output:

```bash
python -m pytest tests/ -v
```

## Usage

```python
from main import sort

# Classify a package
result = sort(width=10.0, height=10.0, length=10.0, mass=10.0)
print(result)  # Output: STANDARD

# Heavy package
result = sort(width=10.0, height=10.0, length=10.0, mass=25.0)
print(result)  # Output: SPECIAL

# Bulky and heavy package
result = sort(width=150.0, height=150.0, length=150.0, mass=25.0)
print(result)  # Output: REJECTED
```

## Classification Rules

- **STANDARD**: Neither heavy nor bulky
- **SPECIAL**: Either heavy OR bulky (but not both)
- **REJECTED**: Both heavy AND bulky

## Validation

The package model enforces the following constraints:
- All dimensions (width, height, length) must be > 0 and ≤ 10,000
- Mass must be > 0 and ≤ 1,000
- Negative or zero values are rejected with ValidationError

## Architecture Highlights

- **Separation of Concerns**: Models, enums, and business logic are cleanly separated
- **Type Safety**: Leverages Python type hints and Pydantic's runtime validation
- **Computed Properties**: Package heaviness and bulkiness are calculated on-demand
- **Testability**: Parameterized tests ensure comprehensive coverage of edge cases