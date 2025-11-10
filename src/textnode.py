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

    def __eq__(self, other):
        return (
            self.TextType == other.TextType
            and self.text == other.text
            and self.url == other.url
        )

    def __repr__(self):
        return f'TextNode({self.text}, {self.TextType.value}, {self.url})'