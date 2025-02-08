from enum import Enum

from htmlnode import LeafNode

class TextType(Enum):
    TEXT = "text"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.__text = text
        self.__text_type = TextType(text_type)
        self.__url = url

    def __eq__(self, node):
        left = (self.__text, self.__text_type, self.__url)
        right = (node.get_text(), node.get_text_type(), node.get_url())
        return True if left == right else False

    def get_text(self):
        return self.__text

    def get_text_type(self):
        return self.__text_type

    def get_url(self):
        return self.__url

    def __repr__(self):
        return f'TextNode({self.__text}, {self.__text_type.value}, {self.__url})'
    
def text_node_to_html_node(text_node):
        match text_node.get_text_type():
            case TextType.TEXT:
                return LeafNode(None, text_node.get_text())
            case TextType.BOLD:
                return LeafNode("b", text_node.get_text())
            case TextType.ITALIC:
                return LeafNode("i", text_node.get_text())
            case TextType.CODE:
                return LeafNode("code", text_node.get_text())
            case TextType.LINK:
                return LeafNode("a", text_node.get_text(), {"href": text_node.get_url()})
            case TextType.IMAGE:
                return LeafNode("img", "", {"src": text_node.get_url(), "alt": text_node.get_text()})
            case _:
                raise ValueError(f"Unsupported text type: {text_node.get_text_type()}")

