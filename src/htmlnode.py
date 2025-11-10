from textnode import TextNode, TextType

class HTMLNode:
    def __init__(self,tag = None,value = None,children = None,props = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")

    def props_to_html(self):
        if self.props == None:
            return ""
        prop_list = []
        for key in self.props.keys():
            prop_list.append(f' {key}="{self.props[key]}"')
        return "".join(prop_list)
    
    def __repr__(self):
        return f'HTMLNode({self.tag}, {self.value}, children: {self.children}, {self.props})'

class LeafNode(HTMLNode):
    def __init__(self,tag,value,props=None):
        super(LeafNode, self).__init__(tag,value,None,props)
    def to_html(self):
        if not self.value or self.value == None:
            raise ValueError("Leaf nodes need a value")
        if self.tag == None:
            return self.value
        else:
            return f'<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>'
    
    def __repr__(self):
        return f"LeafNode({self.tag}, {self.value}, {self.props})"

class ParentNode(HTMLNode):
    def __init__(self,tag,children,props=None):
        super(ParentNode, self).__init__(tag,None,children,props)
    def to_html(self):
        if not self.tag or self.tag == None:
            raise ValueError("Parent nodes need a tag")
        if self.children == None:
            raise ValueError("Parent nodes need a child")
        else:
            html = f'<{self.tag}{self.props_to_html()}>'
            for child in self.children:
                html += child.to_html()
            html += f'</{self.tag}>'
            return html
    
    def __repr__(self):
        return f"parent({self.tag}, {self.children}, {self.props})"

'''
An HTMLNode without a tag will just render as raw text
An HTMLNode without a value will be assumed to have children
An HTMLNode without children will be assumed to have a value
An HTMLNode without props simply won't have any attributes
'''
#tag - HTML tag name (e.g. "p", "a", "h1", etc.)
#value - (e.g. the text inside a paragraph)
#children - A list of HTMLNode children of this node
#props - dictionary of key-value pairs: attributes of HTML tag. 
#       eg link (<a> tag) might have {"href": "https://www.google.com"}


def text_node_to_html_node(text_node):
    if not text_node.TextType or text_node.TextType == None:
        raise Exception("Not a text type")
    if text_node.TextType == text_node.TextType.TEXT:
        return LeafNode(None,text_node.text)
    elif text_node.TextType == text_node.TextType.BOLD:
        return LeafNode('b',text_node.text)
    elif text_node.TextType == text_node.TextType.ITALIC:
        return LeafNode('i',text_node.text)
    elif text_node.TextType == text_node.TextType.CODE:
        return LeafNode('code',text_node.text,)
    elif text_node.TextType == text_node.TextType.LINK:
        return LeafNode('a',text_node.text,{'href': text_node.url})
    elif text_node.TextType == text_node.TextType.IMAGE:
        return LeafNode('img',"",{'src': text_node.url, 'alt': text_node.text,})
    else:
        raise ValueError(f"invalid text type: {text_node.TextType}")




