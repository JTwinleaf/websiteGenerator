import unittest
from htmlnode import *
from textnode import *
from txt_to_html import *

class TestText2HTML(unittest.TestCase):
    code = TextNode("Hackerman: I'm in...", TextType.CODE)
    link = TextNode("I can guide you to that which knows all", TextType.LINK, "https://www.google.com")
    image = TextNode("I am a beauty, aren't I?", TextType.IMAGE, "https://eskipaper.com/images/landscape-wallpaper-hd-10.jpg")
    def test_text_type_plain(self):
        plain = TextNode("I am plain like a hamburger", TextType.TEXT)
        plain_html = text_node_to_html_node(plain)
        self.assertEqual(plain_html.tag, None)
        self.assertEqual(plain_html.value, "I am plain like a hamburger")
        self.assertEqual(plain_html.props, None)

    def test_text_type_bold(self):
        bold = TextNode("I was born to be bold", TextType.BOLD)
        bold_html = text_node_to_html_node(bold)
        self.assertEqual(bold_html.tag, "b")
        self.assertEqual(bold_html.value, "I was born to be bold")
        self.assertEqual(bold_html.props, None)
    
    def test_text_type_italic(self):
        italic = TextNode("I smell slightly of olives and tomato sauce", TextType.ITALIC)
        italic_html = text_node_to_html_node(italic)
        self.assertEqual = (italic_html.tag, "i")
        self.assertEqual = (italic_html.value, "I smell slightly of olives and tomato sauce")
        self.assertEqual = (italic_html.props, None)
    