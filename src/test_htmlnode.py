import unittest

from htmlnode import HTMLNode, LeafNode, ParentNode


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
            node.get_tag(),
            "div",
        )
        self.assertEqual(
            node.get_value(),
            "I wish I could read",
        )
        self.assertEqual(
            node.get_children(),
            None,
        )
        self.assertEqual(
            node.get_props(),
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

    def test_to_html_parent(self):
        nodeCh1 = LeafNode("b", "Hello!")
        nodeCh2 = LeafNode(None, " Beautiful!")
        nodeCh3 = LeafNode("i", " World!")
        nodeP = ParentNode("p", [nodeCh1, nodeCh2, nodeCh3], None)
        self.assertEqual(nodeP.to_html(), "<p><b>Hello!</b> Beautiful!<i> World!</i></p>")

    def test_to_html_parent_nested(self):
        nodeCh1 = LeafNode("b", "Hello!")
        nodeCh2 = LeafNode(None, " Beautiful!")
        nodeCh3 = LeafNode("i", " World!")
        nodeP1 = ParentNode("div", [nodeCh1, nodeCh2], None)
        nodeP2 = ParentNode("p", [nodeP1, nodeCh3], None)
        self.assertEqual(nodeP2.to_html(), "<p><div><b>Hello!</b> Beautiful!</div><i> World!</i></p>")

    def test_to_html_parent_no_children(self):
        nodeP1 = ParentNode("div", [], None)
        self.assertEqual(nodeP1.to_html(), "<div></div>")

    def test_headings(self):
        node = ParentNode(
            "h2",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        )
        self.assertEqual(
            node.to_html(),
            "<h2><b>Bold text</b>Normal text<i>italic text</i>Normal text</h2>",
        )


    



if __name__ == "__main__":
    unittest.main()