from htmlnode import HTMLNode

class ParentNode(HTMLNode):
    def __init__(self, tag, children, props=None):
        super().__init__(tag=tag, value=None, children=children, props=props)


    def to_html(self):
        if self.tag is None:
            raise ValueError("Node has no tag!")
        
        if self.children is None or self.children == []:
            raise ValueError("Node dose not have and child!")
        
        output = ""
        for child in self.children:
            output += child.to_html()

        if self.props_to_html() == "":
            return f"<{self.tag}>{output}</{self.tag}>"
                
        return f"<{self.tag} {self.props_to_html()}>{output}</{self.tag}>"    


    def __repr__(self):
        return f"ParentNode({self.tag}, children: {self.children}, {self.props})"

