import unittest
from main import extract_title

class TestHTMLNode(unittest.TestCase):
    def test_extract_title(self):
        expected = "Tolkien Fan Club"
        result = extract_title('src/content/index.md')
        self.assertEqual(expected, result)