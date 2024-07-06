import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from plantuml_generator.core import plantuml, generate_uml_png

class TestCore(unittest.TestCase):
    """Test cases for the core module."""

    def test_plantuml(self):
        """Test the plantuml function."""
        uml_code = """
        @startuml
        Alice -> Bob: Hello
        @enduml
        """
        result = plantuml("", uml_code)
        print(result)  # Debug print to see the actual output
        self.assertIsInstance(result, bytes)
        self.assertTrue(result.startswith(b'<svg'), f"Output did not start with '<svg': {result[:50]}")


    def test_generate_uml_png(self):
        """Test the generate_uml_png function."""
        uml_code = """
        @startuml
        Alice -> Bob: Hello
        @enduml
        """
        output_file = "test_output.png"
        generate_uml_png(uml_code, output_file)
        self.assertTrue(os.path.exists(output_file))
        os.remove(output_file)

if __name__ == '__main__':
    unittest.main()
