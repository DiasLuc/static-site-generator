import unittest

from markdowntonode import *
from textnode import TextType, TextNode

class TestTextToHTMLNode(unittest.TestCase):
    def test_delimiter_in_middle(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)

        expected = [
            TextNode("This is text with a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        assert result == expected

    def test_delimiter_at_start(self):
        node = TextNode("`code block` word", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        
        expected = [
            TextNode("code block", TextType.CODE),
            TextNode(" word", TextType.TEXT),
        ]
        assert result == expected

    def test_delimiter_at_end(self):
        node = TextNode("word `code block`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("word ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
        ]
        assert result == expected

    def test_multiple_delimiters(self):
        node = TextNode("Here is `code` and more `code`", TextType.TEXT)
        result = split_nodes_delimiter([node], "`", TextType.CODE)
        expected = [
            TextNode("Here is ", TextType.TEXT),
            TextNode("code", TextType.CODE),
            TextNode(" and more ", TextType.TEXT),
            TextNode("code", TextType.CODE),
        ]
        assert result == expected

    def test_single_delimiter(self):
        node = TextNode("missing closing `delimiter", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "`", TextType.CODE)