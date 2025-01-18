from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("All leaf nodes must have a value")
        if self.tag is None:
            return str(self.value)
        html_string = f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        return html_string
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"



# test = LeafNode("p", "This is a paragraph of text.")
# test2 = LeafNode("a", "Click me!", {"href": "https://www.google.com"})

# print(f"Test should be: <p>This is a paragraph of text.</p>")
# print(f"Test is: {test.to_html()}")
# print(f'Test2 should be: <a href="https://www.google.com">Click me!</a>')
# print(f"Test2 is: {test2.to_html()}")
# print(f"Test2 props_to_html: {test2.props_to_html()}")
# print(f"Test2 repr_: {test2.__repr__()}")

# test3 = LeafNode(tag='a', value=None)
# print(f"REPR: {test3.__repr__()}")
# print(f"TO_HTML: {test3.to_html()}")

# test4 = LeafNode(tag=None, value="This is the value")
# print(f"REPR: {test4.__repr__()}")
# print(f"TO_HTML: {test4.to_html()}")