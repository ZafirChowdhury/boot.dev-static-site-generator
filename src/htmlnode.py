class HTMLNode:
    def __init__(self, tag=None, value=None, children=None, props=None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props


    def to_html(self):
        raise NotImplementedError("Child class did not impliment it")

    # maybe refactor 
    def props_to_html(self):
        if self.prop is None:
            return ""

        output_str = ""

        for key, value in self.props:
            if len(self.props) == 1:
                return f"{key}={value}"
            
            output_str += f"{key}={value} "

        return output_str
    

    def __repr__(self):
        return f"HTMLNode({self.tag}, {self.value}, {self.children}, {self.props})"
