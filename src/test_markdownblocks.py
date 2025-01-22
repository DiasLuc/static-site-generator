import unittest
from markdownblocks import markdown_to_blocks


class TestMarkdownToHTML(unittest.TestCase):
    # Test markdown_to_blocks
    def test_markdown_to_blocks_multiline(self):
        markdown = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item
* This is another list item'''

        expected = ['# This is a heading', 'This is a paragraph of text. It has some **bold** and *italic* words inside of it.', '* This is the first list item in a list block\n* This is a list item\n* This is another list item']
        result = markdown_to_blocks(markdown)
        assert expected == result

    def test_markdown_to_blocks_singleline(self):
        markdown = "  # Header 1  \n\n\nSome text here.  \n\n\n\n  * List item 1 \n* List item 2  "
        expected = ['# Header 1', 'Some text here.', '* List item 1 \n* List item 2']
        result = markdown_to_blocks(markdown)
        assert expected == result
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with *italic* text and `code` here\nThis is the same paragraph on a new line",
                "* This is a list\n* with items",
            ],
        )
