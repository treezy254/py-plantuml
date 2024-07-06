import os
import subprocess
import uuid
import argparse

from .utils import _exec_and_get_paths

PLANTUMLPATH = '/usr/local/bin/plantuml.jar'

def plantuml_exec(*file_names, **kwargs):
    """
    Execute PlantUML jar to generate SVG diagrams.

    This function runs the PlantUML jar file to generate SVG diagrams from the given UML files.

    Args:
        *file_names (str): Variable number of file names to process.
        **kwargs: Arbitrary keyword arguments.

    Keyword Args:
        plantuml_path (str): Path to the PlantUML jar file. Defaults to PLANTUMLPATH.

    Returns:
        list: A list of paths to the generated SVG files.

    Raises:
        subprocess.CalledProcessError: If the PlantUML command fails to execute.
    """
    plantuml_path = kwargs.get('plantuml_path', PLANTUMLPATH)
    cmd = ["java", "-splash:no", "-jar", plantuml_path, "-tsvg"] + list(file_names)
    print(f"Executing command: {' '.join(cmd)}")  # Debug print
    return _exec_and_get_paths(cmd, file_names)


def plantuml_web(*file_names, **kwargs):
    """
    Use PlantUML web service to generate SVG diagrams.

    This function uses the PlantUML web service via the plantweb command to generate SVG diagrams.

    Args:
        *file_names (str): Variable number of file names to process.
        **kwargs: Arbitrary keyword arguments (not used in this function).

    Returns:
        list: A list of paths to the generated SVG files.

    Raises:
        subprocess.CalledProcessError: If the plantweb command fails to execute.
    """
    cmd = ["plantweb", "--format", "auto"] + list(file_names)
    print(f"Executing web command: {' '.join(cmd)}")  # Debug print
    return _exec_and_get_paths(cmd, file_names)


def plantuml(line, cell):
    """
    Generate SVG diagram from PlantUML code.

    This function takes PlantUML code and generates an SVG diagram. It can use either
    the PlantUML jar file or the PlantUML web service.

    Args:
        line (str): Command line arguments for configuring the PlantUML execution.
        cell (str): The PlantUML code to process.

    Returns:
        bytes: The content of the generated SVG file.

    Raises:
        ValueError: If PlantUML fails to generate the SVG.
        argparse.ArgumentError: If the command line arguments are invalid.
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("-j", "--jar", action="store_true", help="render using plantuml.jar (default is plantweb)")
    parser.add_argument("-n", "--name", type=str, default=None, help="persist as .uml and .svg after rendering")
    parser.add_argument("-p", "--plantuml-path", default=None, help=f"specify PlantUML jar path (default={PLANTUMLPATH})")
    args = parser.parse_args(line.split() if line else "")

    base_name = args.name or str(uuid.uuid4())
    use_web = not (args.jar or args.plantuml_path)

    uml_path = base_name + ".uml"
    with open(uml_path, 'w') as fp:
        fp.write(cell)

    try:
        output = None
        if use_web:
            output = plantuml_web(uml_path)
        else:
            plantuml_path = os.path.abspath(args.plantuml_path or PLANTUMLPATH)
            output = plantuml_exec(uml_path, plantuml_path=plantuml_path)

        if output:
            svg_path = output[0]
            with open(svg_path, 'rb') as fp:
                svg_content = fp.read()
            print(f"SVG content: {svg_content[:200]}")  # Debug print
            return svg_content
        else:
            raise ValueError("PlantUML failed to generate SVG")
    finally:
        os.unlink(uml_path)


def generate_uml_png(uml_code, png_file):
    """
    Generate a PNG image from PlantUML code.

    This function takes PlantUML code, generates an SVG diagram, and then converts it to PNG format.

    Args:
        uml_code (str): The PlantUML code to process.
        png_file (str): The path where the generated PNG file should be saved.

    Raises:
        ImportError: If cairosvg is not installed.
        ValueError: If PlantUML fails to generate the SVG.
    """
    try:
        import cairosvg
    except ImportError:
        raise ImportError("cairosvg is required for PNG generation. Please install it with 'pip install cairosvg'.")

    svg_content = plantuml("", uml_code)
    svg_file = "uml_diagram.svg"
    with open(svg_file, "wb") as f:
        f.write(svg_content)
    try:
        cairosvg.svg2png(url=svg_file, write_to=png_file)
    finally:
        os.remove(svg_file)