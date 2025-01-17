from enum import Enum

class TextType(Enum):
    normal_text = 'normal'
    bold_text = 'bold'
    italic_text = 'italic'
    code_text = 'code'
    link = 'link'
    image = 'image'

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = text_type
        self.url = url

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type}, {self.url})"