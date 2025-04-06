from textnode import *
from htmlnode import *
from txt_to_html import *

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    inside_delimiter = False
    formatted_text = ""

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue
        
    parts = node.text.split(delimiter)

    for i, part in enumerate(parts):
        if inside_delimiter:
            formatted_text += part

            if i < len(parts) - 1:
                new_nodes.append(TextNode(formatted_text, text_type))
                formatted_text = ""
                inside_delimiter = False
        
        else:
            new_nodes.append(TextNode(part, TextType.TEXT))

            if i < len(parts) - 1:
                inside_delimiter = True

    if inside_delimiter:
        raise ValueError("Unclosed delimiter found in text node.")

    return new_nodes   