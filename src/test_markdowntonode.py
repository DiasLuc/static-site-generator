import unittest

from markdowntonode import (
    split_nodes_delimiter,
    extract_markdown_images,
    extract_markdown_links,
    split_nodes_image,
    split_nodes_link,
    text_to_textnodes,
)

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

    # extract_markdown_images() test
    def test_extract_image(self):
        text = "This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)"
        assert extract_markdown_images(text) == [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]
    # extract_markdown_links() test
    def test_extract_links(self):
        text = "This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)"
        assert extract_markdown_links(text) == [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]

    # split_nodes_image() tests
    def test_split_node_image_single_image(self):
        test_nodes = [TextNode("Here is an image ![alt](link)", TextType.TEXT)]
        split_nodes = split_nodes_image(test_nodes)
        expected = [
            TextNode("Here is an image ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "link")
        ]
        assert split_nodes == expected

    def test_split_node_image_multiple_images(self):
        test_nodes = [TextNode("Image ![alt1](link1) and ![alt2](link2)", TextType.TEXT)]
        split_nodes = split_nodes_image(test_nodes)
        expected = [
            TextNode("Image ", TextType.TEXT),
            TextNode("alt1", TextType.IMAGE, "link1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("alt2", TextType.IMAGE, "link2")
        ]
        assert split_nodes == expected

    def test_split_node_image_image_at_start(self):
        test_nodes = [TextNode("![alt1](link1) is the first thing", TextType.TEXT)]
        split_nodes = split_nodes_image(test_nodes)
        expected = [
            TextNode("alt1", TextType.IMAGE, "link1"),
            TextNode(" is the first thing", TextType.TEXT),
        ]
        assert split_nodes == expected

    def test_split_node_image_image_at_end(self):
        test_nodes = [TextNode("Image is at the end ![alt](link)", TextType.TEXT)]
        split_nodes = split_nodes_image(test_nodes)
        expected = [
            TextNode("Image is at the end ", TextType.TEXT),
            TextNode("alt", TextType.IMAGE, "link"),
        ]
        assert split_nodes == expected

    def test_split_node_image_no_image(self):
        test_nodes = [TextNode("No images in this node", TextType.TEXT)]
        split_nodes = split_nodes_image(test_nodes)
        expected = [
            TextNode("No images in this node", TextType.TEXT),
        ]
        assert split_nodes == expected

    # split_nodes_link() tests
    def test_split_node_link_single_link(self):
        test_nodes = [TextNode("Here is a link [text](link)", TextType.TEXT)]
        split_nodes = split_nodes_link(test_nodes)
        expected = [
            TextNode("Here is a link ", TextType.TEXT),
            TextNode("text", TextType.LINK, "link")
        ]
        assert split_nodes == expected

    def test_split_node_link_multiple_links(self):
        test_nodes = [TextNode("Link [text1](link1) and [text2](link2)", TextType.TEXT)]
        split_nodes = split_nodes_link(test_nodes)
        expected = [
            TextNode("Link ", TextType.TEXT),
            TextNode("text1", TextType.LINK, "link1"),
            TextNode(" and ", TextType.TEXT),
            TextNode("text2", TextType.LINK, "link2")
        ]
        assert split_nodes == expected

    def test_split_node_link_link_at_start(self):
        test_nodes = [TextNode("[text](link1) is the first thing", TextType.TEXT)]
        split_nodes = split_nodes_link(test_nodes)
        expected = [
            TextNode("text", TextType.LINK, "link1"),
            TextNode(" is the first thing", TextType.TEXT),
        ]
        assert split_nodes == expected

    def test_split_node_link_link_at_end(self):
        test_nodes = [TextNode("Link is at the end [text](link)", TextType.TEXT)]
        split_nodes = split_nodes_link(test_nodes)
        expected = [
            TextNode("Link is at the end ", TextType.TEXT),
            TextNode("text", TextType.LINK, "link"),
        ]
        assert split_nodes == expected

    def test_split_node_link_no_link(self):
        test_nodes = [TextNode("No Links in this node", TextType.TEXT)]
        split_nodes = split_nodes_link(test_nodes)
        expected = [
            TextNode("No Links in this node", TextType.TEXT),
        ]
        assert split_nodes == expected

    # Test text_to_textnodes()
    def test_text_to_textnodes(self):
        expected = [
            TextNode("This is ", TextType.TEXT),
            TextNode("text", TextType.BOLD),
            TextNode(" with an ", TextType.TEXT),
            TextNode("italic", TextType.ITALIC),
            TextNode(" word and a ", TextType.TEXT),
            TextNode("code block", TextType.CODE),
            TextNode(" and an ", TextType.TEXT),
            TextNode("obi wan image", TextType.IMAGE, "https://i.imgur.com/fJRm4Vk.jpeg"),
            TextNode(" and a ", TextType.TEXT),
            TextNode("link", TextType.LINK, "https://boot.dev"),
        ]

        test_text = "This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)"
        actual_result = text_to_textnodes(test_text)
        assert expected == actual_result