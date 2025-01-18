import unittest

from htmlnode import LeafNode


class TestLeafNode(unittest.TestCase):
    def test_children(self):
        node = LeafNode(value=None, tag=None)
        self.assertEqual(node.children, None)

    def test_node_no_value_error(self):
        node = LeafNode(tag='a', value=None)
        self.assertRaises(ValueError, node.to_html)

    def test_node_no_tag(self):
        node = LeafNode(tag=None, value="This is the value")
        expected = "This is the value"
        self.assertEqual(node.to_html(), expected)
    def test_to_html_no_prop(self):
        node = LeafNode("p", "This is a paragraph of text.")
        expected = "<p>This is a paragraph of text.</p>"
        self.assertEqual(node.to_html(), expected)

    def test_to_html_with_prop(self):
        node = LeafNode("a", "Click me!", {"href": "https://www.google.com"})
        expected = '<a href="https://www.google.com">Click me!</a>'
        self.assertEqual(node.to_html(), expected)

if __name__ == "__main__":
    unittest.main()