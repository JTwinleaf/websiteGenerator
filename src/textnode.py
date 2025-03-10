from enum import Enum

class TextType(Enum):
    TEXT = "body"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode:
    def __init__(self, text, text_type, url=None, alt_text=None):
        self.text = text
        self.type = text_type
        self.url = url
        self.alt_text = alt_text
    
    def __repr__(self):
        return f"TextNode({self.text}, {self.text_type.value}, {self.url}, {self.alt_text})"
    
    def __eq__(self, other):
        if not isinstance(other, TextNode):
            raise TypeError("Invalid Input")
        return self.text == other.text and self.type == other.type and self.url == other.url
