import unittest
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode


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
        node2 = TextNode("This is a text node", TextType.QUOTE)
        self.assertNotEqual(node, node2)

        # Check for url passed
        node = TextNode("This is a text node", TextType.PARAGRAPH, 'www.google.com')
        node2 = TextNode("This is a text node", TextType.PARAGRAPH, 'google.com')
        self.assertNotEqual(node, node2)

    def test_text_node_to_html_node(self):
        # Test Normal Text
        node = TextNode('Normal text', TextType.TEXT)
        node2 = LeafNode(None, 'Normal text')
        self.assertEqual(text_node_to_html_node(node).to_html(), node2.to_html())

        # Test Bold Text
        node = TextNode('Bold text', TextType.BOLD)
        node2 = LeafNode('b', 'Bold text')
        self.assertEqual(text_node_to_html_node(node).to_html(), node2.to_html())

        # Test Italic Text
        node = TextNode('Italic text', TextType.ITALIC)
        node2 = LeafNode('i', 'Italic text')
        self.assertEqual(text_node_to_html_node(node).to_html(), node2.to_html())

        # Test Code Text
        node = TextNode('Code text', TextType.CODE)
        node2 = LeafNode('code', 'Code text')
        self.assertEqual(text_node_to_html_node(node).to_html(), node2.to_html())
        
        # Test Link Text
        node = TextNode('Link text', TextType.LINK, 'link_text_url.com')
        node2 = LeafNode('a', 'Link text', {'href': 'link_text_url.com'})
        self.assertEqual(text_node_to_html_node(node).to_html(), node2.to_html())

        # Test Image Text
        node = TextNode('Image text', TextType.IMAGE, 'image_text_url.com')
        node2 = LeafNode('img', '', {'src': 'image_text_url.com', 'alt': 'Image text'})
        self.assertEqual(text_node_to_html_node(node).to_html(), node2.to_html())
