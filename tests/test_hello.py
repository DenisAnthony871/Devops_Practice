import unittest
import sys
from io import StringIO

class TestHelloDevops(unittest.TestCase):
    def setUp(self):
        self.held_output = StringIO()
        self.original_stdout = sys.stdout
        sys.stdout = self.held_output

    def tearDown(self):
        sys.stdout = self.original_stdout

    def test_hello_output(self):
        # Import and run the script
        with open('../hello.py') as f:
            exec(f.read())
        
        self.assertEqual(
            self.held_output.getvalue().strip(),
            "Hello, DevOps!"
        )

if __name__ == '__main__':
    unittest.main()