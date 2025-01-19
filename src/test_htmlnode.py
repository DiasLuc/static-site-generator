import unittest

from htmlnode import *
from textnode import TextType, TextNode


class TestHTMLNode(unittest.TestCase):
    def test_props_to_html(self):
        node = HTMLNode()
        node.props = {
            "href": "https://www.google.com",
            "target": "_blank",
        }
        self.assertEqual(node.props_to_html(), ' href="https://www.google.com" target="_blank"')

    def test_node_no_children_or_props(self):
        node = HTMLNode("p", "This is some text inside a paragraph")
        node2 = HTMLNode()
        node2.tag = 'p'
        node2.value = "This is some text inside a paragraph"
        self.assertEqual(node.__repr__(), node2.__repr__())

    def test_children(self):
        child1 = HTMLNode()
        child2 = HTMLNode()
        parent = HTMLNode(children=[child1, child2])
        self.assertEqual(parent.children, [child1, child2])

    def test_repr(self):
        child = HTMLNode()
        node = HTMLNode("a", "This is the value", [child], {"href": "https://www.google.com"} )
        repr_string = f"-HTMLNode Object-\n Tag: {node.tag}\n Value: {node.value}\n Children: {node.children}\n Props:{node.props}\nProps_to_html:{node.props_to_html()}"
        self.assertEqual(node.__repr__(), repr_string)


class TestTextToHTMLNode(unittest.TestCase):
    def test_text_to_html_node(self):
        # Test basic text node
        text_node = TextNode("Hello, world!", TextType.TEXT)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == None
        assert html_node.value == "Hello, world!"

    def test_bold_to_html_node(self):
        # Test Bold text node
        text_node = TextNode("Bold text", TextType.BOLD)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == "b"
        assert html_node.value == "Bold text"

    def test_italic_to_html_node(self):
        # Test Italic text node
        text_node = TextNode("Italic text", TextType.ITALIC)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == 'i'
        assert html_node.value == "Italic text"    
        
    def test_code_to_html_node(self):
        # Test Code text node
        text_node = TextNode("This is some code", TextType.CODE)
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == 'code'
        assert html_node.value == "This is some code"

    def test_link_to_html_node(self):
        # Test Link text node
        text_node = TextNode("Link Text", TextType.LINK, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == 'a'
        assert html_node.props["href"] == "https://www.boot.dev"
        assert html_node.value == "Link Text"

    def test_image_to_html_node(self):
        # Test Image text node
        text_node = TextNode("Alt Text", TextType.IMAGE, "https://www.boot.dev")
        html_node = text_node_to_html_node(text_node)
        assert html_node.tag == 'img'
        assert html_node.props["src"] == "https://www.boot.dev"
        assert html_node.props["alt"] == "Alt Text"
    
    def test_invalid_to_html_nodes(self):
        # Test Invalid text node
        text_node = TextNode("Alt Text", "INVALID", "https://www.boot.dev")
        with self.assertRaises(Exception):
            text_node_to_html_node(text_node)
if __name__ == "__main__":
    unittest.main()