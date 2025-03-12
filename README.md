# PythonPlantuml

PythonPlantUML Generator is a Python library for generating UML diagrams using PlantUML. It provides a simple interface to create SVG and PNG diagrams from PlantUML code.
 
## Installation 
  
You can install the PlantUML Generator using pip:
```   
pip install pythonplantuml 
```  

## Usage 

Here's a basic example of how to use the PlantUML Generator:

```python
from pythonplantuml import generate_uml_png

uml_code = """
@startuml
Alice -> Bob: Hello
Bob --> Alice: Hi!
@enduml
"""

generate_uml_png(uml_code, "output.png")
```

This will generate a PNG file named "output.png" with the UML diagram.

## Features

- Generate SVG diagrams from PlantUML code
- Convert SVG diagrams to PNG
- Support for both local PlantUML jar and PlantUML web service

## Documentation
For more detailed information about the PlantUML Generator, please refer to the full documentation.

## Development
To set up the development environment:


Clone the repository
Install the development dependencies:

```
pip install -r requirements.txt
```

Run the tests:
```
python -m unittest discover tests
```

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

### License
This project is licensed under the MIT License - see the LICENSE file for details.
