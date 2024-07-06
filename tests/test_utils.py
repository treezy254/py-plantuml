import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import unittest
from plantuml_generator.utils import _exec_and_get_paths

class TestUtils(unittest.TestCase):
    """Test cases for the utils module."""

    def test_exec_and_get_paths(self):
        """Test the _exec_and_get_paths function."""
        # This is a mock test, as we can't easily test the actual function
        file_names = ["test1.uml", "test2.uml"]
        expected_output = ["test1.svg", "test2.svg"]
        
        # Mock the subprocess.check_call
        def mock_check_call(cmd, shell, stderr):
            pass
        
        # Replace the actual function with our mock
        import subprocess
        original_check_call = subprocess.check_call
        subprocess.check_call = mock_check_call
        
        try:
            result = _exec_and_get_paths(["mock_command"], file_names)
            self.assertEqual(result, expected_output)
        finally:
            # Restore the original function
            subprocess.check_call = original_check_call

if __name__ == '__main__':
    unittest.main()
