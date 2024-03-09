# Pythonisms Project

## Overview

The Pythonisms project demonstrates the use of pythonic language features, including iterators/generators, decorators, and dunder methods. This project not only showcases these features through practical examples but also includes tests written with `pytest` to ensure the functionality works as expected.

## Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package installer)

### Setting Up the Project

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd pythonisms
   ```

2. **Create and activate a virtual environment:**

   - On macOS/Linux:

     ```bash
     python3 -m venv .venv
     source .venv/bin/activate
     ```

   - On Windows:

     ```bash
     python -m venv .venv
     .venv\Scripts\activate
     ```

3. **Install dependencies:**

   ```bash
   pip install pytest
   ```

### Project Structure

- `custom_collection.py`: Implements a custom collection class that supports iteration.
- `decorators.py`: Contains decorators for adding behavior to functions.
- `custom_data.py`: Defines a custom data structure with dunder methods for equality and truthiness.
- `test_pythonisms.py`: Contains `pytest` tests for each component of the project.

## Running the Tests

Ensure you are in the project directory and your virtual environment is activated. Run the tests using the following command:

```bash
pytest
```

`pytest` will automatically find and execute all test functions defined in `test_pythonisms.py`, and report the results.

## Features

- **Custom Collection:** Demonstrates how to make a custom collection iterable, allowing it to be used in for loops, list comprehensions, and conversion to list or other collection types.

- **Decorators:** Showcases decorators for timing functions, logging call information, slowing down function execution, and modifying return values.

- **Dunder Methods:** Uses dunder methods to make custom data structures comparable for equality, and to evaluate their truthiness.



