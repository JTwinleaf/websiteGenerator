import unittest
from htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(props={"href":"https://twinleaf.town"})
        node2 = HTMLNode(props={"href":"https://twinleaf.town"})
        self.assertEqual(node.props_to_html(), node2.props_to_html())
    
    def test_noteq(self):
        node = HTMLNode(props={"href":"https://twinleaf.town"})
        node2 = HTMLNode(props={"href":"https://google.com"})
        self.assertNotEqual(node.props_to_html(), node2.props_to_html())
    
    def test_isnone(self):
        node = HTMLNode()
        self.assertIsNone(node.props_to_html())

if __name__ == "__main__":
    unittest.main()