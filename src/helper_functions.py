from textnode import TextType, TextNode
from leafnode import LeafNode

import re

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

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue
            
        nodes = []
        parts = old_node.text.split(delimiter)
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


def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)


def split_nodes_image(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)

        original_string = old_node.text
        images = extract_markdown_images(original_string)

        if len(images) == 0:
            new_nodes.append(old_node)
            continue

        for image in images:
            parts = original_string.split(f"![{image[0]}]({image[1]})", 1)

            if len(parts) != 2:
                raise ValueError("Invalid Markdown, Open image tag not closed!")
            
            if parts[0] != "":
                new_nodes.append(TextNode(text=parts[0], text_type=TextType.TEXT))
            
            new_nodes.append(TextNode(text=image[0], url=image[1], text_type=TextType.IMAGE))

            original_string = parts[1]

        if original_string != "":
            new_nodes.append(TextNode(text=original_string, text_type=TextType.TEXT))

    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []

    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)

        original_string = old_node.text
        links = extract_markdown_links(original_string)

        if len(links) == 0:
            new_nodes.append(old_node)
            continue

        for link in links:
            parts = original_string.split(f"[{link[0]}]({link[1]})", 1)

            if len(parts) != 2:
                raise ValueError("Invalid Markdown, Open link tag not closed!")
            
            if parts[0] != "":
                new_nodes.append(TextNode(text=parts[0], text_type=TextType.TEXT))
            
            new_nodes.append(TextNode(text=link[0], url=link[1], text_type=TextType.LINK))

            original_string = parts[1]

        if original_string != "":
            new_nodes.append(TextNode(text=original_string, text_type=TextType.TEXT))

    return new_nodes
