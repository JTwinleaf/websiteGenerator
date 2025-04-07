import unittest
from website_generator.src.htmlnode import *
from website_generator.src.textnode import *
from website_generator.src.markdown_to_textnode import *

def test_code_delimiter():
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
    
    assert len(new_nodes) == 3
    assert new_nodes[0].text == "This is text with a "
    assert new_nodes[0].text_type == TextType.TEXT
    assert new_nodes[1].text == "code block"
    assert new_nodes[1].text_type == TextType.CODE
    assert new_nodes[2].text == " word"
    assert new_nodes[2].text_type == TextType.TEXT

def test_bold_delimiter():
    # Test with bold delimiters
    pass

def test_italic_delimiter():
    # Test with italic delimiters
    pass

def test_multiple_delimiters():
    # Test text with multiple instances of same delimiter
    pass

def test_missing_closing_delimiter():
    # Test that an exception is raised when closing delimiter is missing
    pass

def test_non_text_nodes():
    # Test that non-TEXT nodes are passed through unchanged
    pass

# Add more test cases as needed