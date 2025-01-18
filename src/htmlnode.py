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
    
