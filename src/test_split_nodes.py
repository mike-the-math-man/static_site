import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode, text_node_to_html_node
from textnode import TextNode, TextType
from split_delimeter import split_nodes_delimiter

class TestSplitDelimeter(unittest.TestCase):
    def test_delimeter_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, 
                         [TextNode("This is text with a ", TextType.TEXT), TextNode("code block", TextType.CODE),TextNode(" word", TextType.TEXT),])

    def test_delimeter_bolds(self):
        node = TextNode("This is text has **two** bold **words**", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertEqual(new_nodes, 
                         [TextNode("This is text has ", TextType.TEXT), TextNode("two", TextType.BOLD),TextNode(" bold ", TextType.TEXT),TextNode("words", TextType.BOLD),])
    
    def test_delimeter_invalid_syntax(self):
        node = TextNode("This is text has **incorrect bold word", TextType.TEXT)
        with self.assertRaises(Exception):
            split_nodes_delimiter([node], "**", TextType.BOLD)

    def test_delimeter_text(self):
        node = TextNode("link", TextType.LINK)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertEqual(new_nodes, 
                         [TextNode("link", TextType.LINK)])

    def test_delimeter_multiple(self):
        node = TextNode("this **bold** thing", TextType.TEXT)
        node2 = TextNode("this `code` thing", TextType.TEXT)
        node3 = TextNode("this **bold** and `cold` thing", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node,node2,node3], "**", TextType.BOLD)
        self.assertEqual(new_nodes, 
                         [TextNode("this ", TextType.TEXT),
                          TextNode("bold", TextType.BOLD),
                          TextNode(" thing", TextType.TEXT),
                          TextNode("this `code` thing",TextType.TEXT),
                          TextNode("this ", TextType.TEXT),
                          TextNode("bold", TextType.BOLD),
                          TextNode(" and `cold` thing", TextType.TEXT)])

    def test_delim_bold(self):
        node = TextNode("This is text with a **bolded** word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_double(self):
        node = TextNode(
            "This is text with a **bolded** word and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded", TextType.BOLD),
                TextNode(" word and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_bold_multiword(self):
        node = TextNode(
            "This is text with a **bolded word** and **another**", TextType.TEXT
        )
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("bolded word", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("another", TextType.BOLD),
            ],
            new_nodes,
        )

    def test_delim_italic(self):
        node = TextNode("This is text with an _italic_ word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("This is text with an ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )

    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertListEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

    def test_delim_code(self):
        node = TextNode("This is text with a `code block` word", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
        self.assertListEqual(
            [
                TextNode("This is text with a ", TextType.TEXT),
                TextNode("code block", TextType.CODE),
                TextNode(" word", TextType.TEXT),
            ],
            new_nodes,
        )
    
    def test_delim_bold_and_italic(self):
        node = TextNode("**bold** and _italic_", TextType.TEXT)
        new_nodes = split_nodes_delimiter([node], "**", TextType.BOLD)
        new_nodes = split_nodes_delimiter(new_nodes, "_", TextType.ITALIC)
        self.assertEqual(
            [
                TextNode("bold", TextType.BOLD),
                TextNode(" and ", TextType.TEXT),
                TextNode("italic", TextType.ITALIC),
            ],
            new_nodes,
        )

if __name__ == "__main__":
    unittest.main()