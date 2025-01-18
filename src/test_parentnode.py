import unittest

from htmlnode import ParentNode, LeafNode


class TestParentNode(unittest.TestCase):

    def test_node_no_tag_error(self):
        node = ParentNode(tag=None,children=LeafNode("b", "Bold text"))
        self.assertRaises(ValueError, node.to_html)
    def test_node_no_children_error(self):
        node = ParentNode(tag="p",children=None)
        self.assertRaises(ValueError, node.to_html)

    def test_single_level_children(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        expected = "<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>"
        self.assertEqual(node.to_html(), expected)
    
    def test_double_level_children(self):
        node = ParentNode(
            "body",
            [
                ParentNode("p",
                    [
                        LeafNode("b", "Bold text"),
                        LeafNode(None, "Normal text"),
                        LeafNode("i", "italic text"),
                        LeafNode(None, "Normal text"),
                    ],    
                )
            ],
        )
        expected = "<body><p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p></body>"
        self.assertEqual(node.to_html(), expected)

        def test_headings(self):
            node = ParentNode(
                "h2",
                [
                    LeafNode("b", "Bold text"),
                    LeafNode(None, "Normal text"),
                    LeafNode("i", "italic text"),
                    LeafNode(None, "Normal text"),
                ],
            )
            self.assertEqual(
                node.to_html(),
                "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
            )

if __name__ == "__main__":
    unittest.main()