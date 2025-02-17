
class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplementedError("Invalid")
    
    def props_to_html(self):
        props = self.props
        output = ""
        if props == None:
            return
        for key in props:
            output += f' {key}="{props[key]}"'
        return output
    
    def __repr__(self):
        pass