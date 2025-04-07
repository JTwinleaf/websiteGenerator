import unittest
from website_generator.src.htmlnode import *


class TestHTMLNode(unittest.TestCase):
    def test_to_html_props(self):
        node = HTMLNode(
            "div",
            "Hello, world!",
            None,
            {"class": "greeting", "href": "https://boot.dev"},
        )
        self.assertEqual(
            node.props_to_html(),
            ' class="greeting" href="https://boot.dev"',
        )

    def test_values(self):
        node = HTMLNode(
            "div",
            "I wish I could read",
        )
        self.assertEqual(
            node.tag,
            "div",
        )
        self.assertEqual(
            node.value,
            "I wish I could read",
        )
        self.assertEqual(
            node.children,
            None,
        )
        self.assertEqual(
            node.props,
            None,
        )

    def test_repr(self):
        node = HTMLNode(
            "p",
            "What a strange world",
            None,
            {"class": "primary"},
        )
        self.assertEqual(
            node.__repr__(),
            "HTMLNode(p, What a strange world, children: None, {'class': 'primary'})",
        )

    def test_to_html_no_children(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

    def test_to_html_no_tag(self):
        node = LeafNode(None, "Hello, world!")
        self.assertEqual(node.to_html(), "Hello, world!")
    
    def test_parent_with_single_child(self):
        child = LeafNode("b", "bold text")
        parent = ParentNode("p", [child])
        self.assertEqual(parent.to_html(), "<p><b>bold text</b></p>")

    def test_parent_with_multiple_children(self):
        child1 = LeafNode("b", "bold")
        child2 = LeafNode("i", "italic")
        parent = ParentNode("p", [child1, child2])
        self.assertEqual(parent.to_html(), "<p><b>bold</b><i>italic</i></p>")

    def test_missing_tag_error(self):
        with self.assertRaises(ValueError):
            ParentNode(None, [LeafNode("span", "text")]).to_html()

    def test_with_properties(self):
        child = LeafNode("span", "text")
        parent = ParentNode("div", [child], {"class": "container"})
        self.assertEqual(parent.to_html(), '<div class="container"><span>text</span></div>')
    
    def test_complex_structure(self):
        leaf1 = LeafNode("b", "bold text")
        leaf2 = LeafNode(None, "normal text")
        inner_parent = ParentNode("div", [
            LeafNode("i", "italic text"),
            LeafNode("u", "underlined text")
        ], {"class": "inner"})
        
        parent = ParentNode("div", [leaf1, leaf2, inner_parent], {"id": "main"})
        
        expected_html = '<div id="main"><b>bold text</b>normal text<div class="inner"><i>italic text</i><u>underlined text</u></div></div>'
        self.assertEqual(parent.to_html(), expected_html)
    
    def test_empty_children_list_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", []).to_html()

    def test_none_children_error(self):
        with self.assertRaises(ValueError):
            ParentNode("div", None).to_html()

    def test_deeply_nested_structure(self):
        level3 = ParentNode("div", [LeafNode("span", "deepest")])
        level2 = ParentNode("div", [level3])
        level1 = ParentNode("div", [level2])
        
        expected = "<div><div><div><span>deepest</span></div></div></div>"
        self.assertEqual(level1.to_html(), expected)

    def test_mixed_leaf_and_parent_children(self):
        leaf = LeafNode("b", "bold")
        inner_parent = ParentNode("div", [LeafNode("i", "italic")])
        parent = ParentNode("p", [leaf, inner_parent])
        
        expected = "<p><b>bold</b><div><i>italic</i></div></p>"
        self.assertEqual(parent.to_html(), expected)

    def test_with_leaf_nodes_without_tags(self):
        # Testing how text nodes without tags are handled
        parent = ParentNode("p", [
            LeafNode("b", "bold"),
            LeafNode(None, " normal "),
            LeafNode("i", "italic")
        ])
        expected = "<p><b>bold</b> normal <i>italic</i></p>"
        self.assertEqual(parent.to_html(), expected)

    def test_with_multiple_props(self):
        # Testing multiple properties
        parent = ParentNode("div", [LeafNode("span", "text")], 
                            {"id": "main", "class": "container", "data-test": "value"})
        self.assertTrue(' id="main"' in parent.to_html())
        self.assertTrue(' class="container"' in parent.to_html())
        self.assertTrue(' data-test="value"' in parent.to_html())
        self.assertTrue(parent.to_html().startswith("<div"))
        self.assertTrue(parent.to_html().endswith("</div>"))

    def test_parent_constructor_requirements(self):
        # Ensure constructor requires tag and children
        with self.assertRaises(TypeError):
            ParentNode()  # Missing required arguments
        
        # These should not raise errors
        ParentNode("div", [])
        ParentNode("div", [], {})

if __name__ == "__main__":
    unittest.main()