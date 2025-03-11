import unittest
from htmlnode import *
from textnode import *
from txt_to_html import *

class TestText2HTML(unittest.TestCase):

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
        self.assertEqual(italic_html.tag, "i")
        self.assertEqual(italic_html.value, "I smell slightly of olives and tomato sauce")
        self.assertEqual(italic_html.props, None)
    
    def test_text_type_code(self):
        code = TextNode("Hackerman: I'm in...", TextType.CODE)
        code_html = text_node_to_html_node(code)
        self.assertEqual(code_html.tag, "code")
        self.assertEqual(code_html.value, "Hackerman: I'm in...")
        self.assertEqual(code_html.props, None)
    
    def test_text_type_link(self):
        link = TextNode("I can guide you to that which knows all", TextType.LINK, "https://www.google.com")
        link_html = text_node_to_html_node(link)
        self.assertEqual(link_html.tag, "a")
        self.assertEqual(link_html.value, "I can guide you to that which knows all")
        self.assertEqual(link_html.props, {"href":"https://www.google.com"})
    
    def test_text_type_image(self):
        image = TextNode("", TextType.IMAGE, "https://eskipaper.com/images/landscape-wallpaper-hd-10.jpg", "OwO What's this?")
        image_html = text_node_to_html_node(image)
        self.assertEqual(image_html.tag, "img")
        self.assertEqual(image_html.value, "")
        self.assertEqual(image_html.props, {"src": "https://eskipaper.com/images/landscape-wallpaper-hd-10.jpg", "alt": "OwO What's this?"})
    
    def test_link_no_url(self):
        node = TextNode("I go nowhere!", TextType.LINK)
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)
    
    def test_no_text_type(self):
        node = TextNode("I am broken...", TextType.NONE)
        with self.assertRaises(ValueError):
            html_node = text_node_to_html_node(node)