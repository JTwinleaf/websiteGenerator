import unittest

from website_generator.src.textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_noteq(self):
        node = TextNode("This is a miror", TextType.BOLD)
        node2 = TextNode("You are a typo", TextType.TEXT)
        self.assertNotEqual(node, node2)
    
    def test_isinstance(self):
        node = TextNode("I am not a TextNode", TextType.TEXT)
        self.assertIsNone(node.url)

if __name__ == "__main__":
    unittest.main()