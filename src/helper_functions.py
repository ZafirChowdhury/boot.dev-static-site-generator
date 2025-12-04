from textnode import TextType, TextNode
from leafnode import LeafNode

def text_node_to_html_node(text_node):
    if text_node.text_type == TextType.TEXT:
        return LeafNode(tag=None, value=text_node.text)
    
    if text_node.text_type == TextType.BOLD:
        return LeafNode(tag="b", value=text_node.text)
    
    if text_node.text_type == TextType.ITALIC:
        return LeafNode(tag="i", value=text_node.text)
    
    if text_node.text_type == TextType.CODE:
        return LeafNode(tag="code", value=text_node.text)
    
    if text_node.text_type == TextType.LINK:
        return LeafNode(tag="a", value=text_node.text, props={"href": text_node.url})
    
    if text_node.text_type == TextType.IMAGE:
        props = {
            "src": text_node.url,
            "alt": text_node.text
        }
        return LeafNode(tag="img", value="", props=props)

    raise Exception("Invalid TextType!")


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
            
        nodes = []
        parts = node.text.split(delimiter)
        if len(parts) % 2 == 0:
            raise ValueError("Invalid markdown, formatted section is not closed")
        
        for i in range(len(parts)):
            if parts[i] == "":
                continue

            if i % 2 != 0:
                nodes.append(TextNode(parts[i], text_type))

            else:
                nodes.append(TextNode(parts[i], TextType.TEXT))

        new_nodes.extend(nodes)

    return new_nodes
