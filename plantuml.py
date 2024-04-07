import os
import subprocess
import uuid
import argparse

# Define the default PlantUML jar path
PLANTUMLPATH = '/usr/local/bin/plantuml.jar'

# Define a function to execute the PlantUML jar and get the paths to the generated SVG files
def _exec_and_get_paths(cmd, file_names):
    subprocess.check_call(cmd, shell=False, stderr=subprocess.STDOUT)
    return [os.path.splitext(f)[0] + ".svg" for f in file_names]

# Define a function to generate SVG diagrams using the PlantUML jar
def plantuml_exec(*file_names, **kwargs):
    """
    Given a list of UML documents, generate corresponding SVG diagrams.

    :param file_names: the filenames of the documents for parsing by PlantUML.
    :param kwargs: optionally `plantuml_path`, indicating where the PlantUML jar file resides.
    :return: the path to the generated SVG UML diagram.
    """
    plantuml_path = kwargs.get('plantuml_path', PLANTUMLPATH)
    cmd = ["java", "-splash:no", "-jar", plantuml_path, "-tsvg"] + list(file_names)
    return _exec_and_get_paths(cmd, file_names)

# Define a function to generate SVG diagrams using the PlantUML web service
def plantuml_web(*file_names, **kwargs):
    """
    Given a list of UML documents, generate corresponding SVG diagrams, using PlantUML's web service via the plantweb module.

    :param file_names: the filenames of the documents for parsing by PlantUML.
    :return: the path to the generated SVG UML diagram.
    """
    cmd = ["plantweb", "--format", "auto"] + list(file_names)
    return _exec_and_get_paths(cmd, file_names)

def plantuml(line, cell):
    """
    Generate and inline the SVG portrayal of the given PlantUML UML spec.

    :param line: if not empty, it is the base file name to give to the serialized cell contents and the generated SVG files.
    :param cell: the PlantUML language UML specification.
    :return: the content of SVG file.
    """
    # Parse the command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--jar", action="store_true", help="render using plantuml.jar (default is plantweb)")
    parser.add_argument("-n", "--name", type=str, default=None, help="persist as .uml and .svg after rendering")
    parser.add_argument("-p", "--plantuml-path", default=None, help="specify PlantUML jar path (default={})".format(PLANTUMLPATH))
    args = parser.parse_args(line.split() if line else "")

    # Generate a base file name for the generated files
    base_name = args.name or str(uuid.uuid4())

    # Determine whether to use the web service or the jar file
    use_web = not (args.jar or args.plantuml_path)

    # Generate the PlantUML UML document file
    uml_path = base_name + ".uml"
    with open(uml_path, 'w') as fp:
        fp.write(cell)

    try:
        # Generate the SVG diagram
        output = None
        if use_web:
            output = plantuml_web(uml_path)
        else:
            plantuml_path = os.path.abspath(args.plantuml_path or PLANTUMLPATH)
            output = plantuml_exec(uml_path, plantuml_path=plantuml_path)

        # Read the SVG diagram
        if output:
            svg_path = output[0]
            with open(svg_path, 'rb') as fp:
                svg_content = fp.read()
            return svg_content
        else:
            raise ValueError("PlantUML failed to generate SVG")
    finally:
        # Clean up the generated files
        os.unlink(uml_path)


# ----
        
# from plantuml_magic import plantuml

import cairosvg
import os

def generate_uml_png(uml_code, png_file):
    """
    Generate a UML diagram as a PNG file from the given PlantUML code.

    :param uml_code: The PlantUML code for the diagram.
    :param png_file: The path to save the output PNG file.
    """
    # Generate the UML diagram
    svg_content = plantuml("", uml_code)

    # Save the SVG content to a file
    svg_file = "uml_diagram.svg"
    with open(svg_file, "wb") as f:
        f.write(svg_content)

    try:
        # Convert the SVG file to a PNG file
        cairosvg.svg2png(url=svg_file, write_to=png_file)
    finally:
        # Remove the SVG file after conversion
        os.remove(svg_file)

# Example usage
uml_code = """
@startuml
Alice -> Bob: Authentication Request
Bob --> Alice: Authentication Response
@enduml
"""
generate_uml_png(uml_code, "uml_diagrams.png")

