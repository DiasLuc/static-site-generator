import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node1 = TextNode("Text node1", TextType.ITALIC)
        node2 = TextNode("Text node2", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_diff_text_type(self):
        node1 = TextNode("Text node", TextType.BOLD)
        node2 = TextNode("Text node", TextType.ITALIC)
        self.assertNotEqual(node1, node2)

    def test_diff_url(self):
        node1 = TextNode("Text node", TextType.BOLD, "http://www.google.com")
        node2 = TextNode("Text node", TextType.ITALIC, "http://www.yahoo.com")
        self.assertNotEqual(node1, node2)

if __name__ == "__main__":
    unittest.main()