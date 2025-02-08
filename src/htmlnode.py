from functools import reduce

class HTMLNode():
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.__tag = tag
        self.__value = value
        self.__children = children
        self.__props = props

    def to_html(self):
        raise NotImplementedError("to_html method not implemented")
    
    def props_to_html(self):
        if self.__props is None:
            return ""
        props_html = ""
        for prop in self.__props:
            props_html += f' {prop}="{self.__props[prop]}"'
        return props_html
    
    def __repr__(self):
        return f"HTMLNode({self.__tag}, {self.__value}, children: {self.__children}, {self.__props})"
    
    def get_tag(self):
        return self.__tag
    
    def get_value(self):
        return self.__value
    
    def get_children(self):
        return self.__children
    
    def get_props(self):
        return self.__props
    
class LeafNode(HTMLNode):
    def __init__(self, tag, value, props=None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.get_value() == None:
            raise ValueError("invalid HTML: no value")
        if self.get_tag() == None:
            return self.get_value()
        return f'<{self.get_tag()}{self.props_to_html()}>{self.get_value()}</{self.get_tag()}>'
    
    def __repr__(self):
        return f'LeafNode({self.get_tag()}, {self.get_value()}, {self.get_props()})'

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag, None, children, props)

    def to_html(self):
        if self.get_tag() == None:
            raise ValueError("invalid HTML: no tag")
        if self.get_children() == None:
            raise ValueError("invalid HTML: no children")
        return f'<{self.get_tag()}>{reduce(lambda acc, child: acc+child.to_html(), self.get_children(), "")}</{self.get_tag()}>'
    
    def __repr__(self):
        return f'ParentNode({self.get_tag()}, children: {self.get_children()}, {self.get_props()})'