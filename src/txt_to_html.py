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
    