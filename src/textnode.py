from enum import Enum

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

