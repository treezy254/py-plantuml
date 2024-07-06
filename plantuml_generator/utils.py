import os
import subprocess

def _exec_and_get_paths(cmd, file_names):
    """
    Execute a command and return paths to generated SVG files.

    Args:
        cmd (list): The command to execute.
        file_names (list): List of input file names.

    Returns:
        list: Paths to the generated SVG files.

    Raises:
        subprocess.CalledProcessError: If the command execution fails.
    """
    subprocess.check_call(cmd, shell=False, stderr=subprocess.STDOUT)
    return [os.path.splitext(f)[0] + ".svg" for f in file_names]