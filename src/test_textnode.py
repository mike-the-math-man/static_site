import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a bold node", TextType.BOLD)
        node2 = TextNode("This is a bold node", TextType.BOLD)
        self.assertEqual(node, node2)
    
    def test_eq2(self):
        node = TextNode("This is a italic node", TextType.ITALIC)
        node2 = TextNode("This is a italic node", TextType.ITALIC)
        self.assertEqual(node, node2)
    
    def test_eq3(self):
        node = TextNode("This is a text node", TextType.TEXT)
        node2 = TextNode("This is a text node", TextType.TEXT)
        self.assertEqual(node, node2)
    
    def test_eq4(self):
        node = TextNode("This is a code node", TextType.CODE)
        node2 = TextNode("This is a code node", TextType.CODE)
        self.assertEqual(node, node2)

    def test_eq5(self):
        node = TextNode("This is a link node", TextType.LINK)
        node2 = TextNode("This is a link node", TextType.LINK)
        self.assertEqual(node, node2)

    def test_eq6(self):
        node = TextNode("This is a text node", TextType.IMAGE,'www.google.com')
        node2 = TextNode("This is a text node", TextType.IMAGE, 'www.google.com')
        self.assertEqual(node, node2)

    def test_neq(self):
        node = TextNode("Jiggly",TextType.TEXT)
        node2 = TextNode("not Jiggly",TextType.TEXT)
        self.assertNotEqual(node,node2)

    def test_neq2(self):
        node = TextNode("Jiggly",TextType.BOLD)
        node2 = TextNode("Jiggly",TextType.TEXT)
        self.assertNotEqual(node,node2)
    
    def test_neq3(self):
        node = TextNode("Jiggly",TextType.BOLD)
        node2 = TextNode("Jiggly",TextType.ITALIC)
        self.assertNotEqual(node,node2)

    def test_neq4(self):
        node = TextNode("Jiggly",TextType.BOLD)
        node2 = TextNode("Jiggly",TextType.LINK)
        self.assertNotEqual(node,node2) 

    def test_neq5(self):
        node = TextNode("Jiggly",TextType.TEXT,'www.google.com')
        node2 = TextNode("Jiggly",TextType.TEXT,'www.yahoo.com')
        self.assertNotEqual(node,node2)


if __name__ == "__main__":
    unittest.main()

