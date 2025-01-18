import unittest

from htmlnode import HTMLNode


class TestTextNode(unittest.TestCase):
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

if __name__ == "__main__":
    unittest.main()