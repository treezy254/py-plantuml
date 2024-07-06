import unittest
import os
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
        self.assertIsInstance(result, bytes)
        self.assertTrue(result.startswith(b'<?xml'))

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