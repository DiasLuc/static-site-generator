class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        html_string = ""
        if self.props != None:
            for prop in self.props:
                html_string += f' {prop}="{self.props[prop]}"'
        return html_string
    def __repr__(self):
        repr_string = f"-HTMLNode Object-\n Tag: {self.tag}\n Value: {self.value}\n Children: {self.children}\n Props:{self.props}\n"
        if self.props != None:
            repr_string +=  f"Props_to_html:{self.props_to_html()}"
        return repr_string
    
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


class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)
    def to_html(self):
        if self.tag is None:
            raise ValueError("All Parent nodes must have a Tag")
        if self.children is None:
            raise ValueError("All Parent nodes must have Children")
        children_html_string = ""
        
        for child in self.children:
            if isinstance(child, LeafNode):
                children_html_string += child.to_html()
                
            if isinstance(child, ParentNode):
                children_html_string += child.to_html()
                
        html_string = f"<{self.tag}{self.props_to_html()}>{children_html_string}</{self.tag}>"
        return html_string
    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"
    
    