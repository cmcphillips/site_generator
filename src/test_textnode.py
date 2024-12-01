import unittest
from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

        # Check for None url passed
        node = TextNode("This is a text node", TextType.PARAGRAPH, None)
        node2 = TextNode("This is a text node", TextType.PARAGRAPH)
        self.assertEqual(node, node2)

        # Check for url passed
        node = TextNode("This is a text node", TextType.PARAGRAPH, 'www.google.com')
        node2 = TextNode("This is a text node", TextType.PARAGRAPH, 'www.google.com')
        self.assertEqual(node, node2)        
    
    def test_neq(self):
        # Check for different strings
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is not a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)
        
        # Check for different Types
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.PARAGRAPH)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.PARAGRAPH)
        node2 = TextNode("This is a text node", TextType.ITALIC)
        self.assertNotEqual(node, node2)

        node = TextNode("This is a text node", TextType.PARAGRAPH)
        node2 = TextNode("This is a text node", TextType.QOUTE)
        self.assertNotEqual(node, node2)

        # Check for url passed
        node = TextNode("This is a text node", TextType.PARAGRAPH, 'www.google.com')
        node2 = TextNode("This is a text node", TextType.PARAGRAPH, 'google.com')
        self.assertNotEqual(node, node2)


