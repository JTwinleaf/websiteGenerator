from htmlnode import *
from textnode import *
from enum import Enum

def text_node_to_html_node(text_node):
    type_dict = {
        TextType.TEXT: (None, None),  
        TextType.BOLD: ("b", None),  
        TextType.ITALIC: ("i", None),
        TextType.CODE: ("code", None),
        TextType.LINK: ("a", {"href": None}),  
        TextType.IMAGE: ("img", {"src": None, "alt": None})  
    }
    if text_node.type not in type_dict: # Checks for any unsupported types
        raise ValueError(f"Unsupported TextType: {text_node.type}")
    tag, props = type_dict[text_node.type]

    if text_node.type == TextType.LINK:
        if text_node.url == None:
            raise ValueError("URL required.")
        props["href"] = text_node.url
        return LeafNode(tag, text_node.text, props)
    elif text_node.type == TextType.IMAGE:
        if text_node.url == None:
            raise ValueError("Image source required.")
        props["src"] = text_node.url
        props["alt"] = text_node.alt_text
        return LeafNode(tag, text_node.text, props)
    
    return LeafNode(tag, text_node.text)