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