from enum import Enum

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"


class TextNode:
    def __init__(self,text,TextType,url = None):
        self.text = text
        self.TextType = TextType
        self.url = url

    def __eq__(node1, node2):
        if node1.text == node2.text and node1.TextType == node2.TextType and node1.url == node2.url:
            return True
        else:
            return False

    def __repr__(self):
        return f'TextNode({self.text}, {self.TextType.value}, {self.url})'