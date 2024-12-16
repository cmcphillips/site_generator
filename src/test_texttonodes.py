import unittest
from textnode import text_node_to_html_node
from texttonodes import text_to_textnodes, TextType, TextNode, list_to_textnodes
from htmlnode import LeafNode

class TestTextToNodes(unittest.TestCase):
    def test_textToNodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        expected_results = [
            TextNode('This is ', TextType.TEXT),
            TextNode('text', TextType.BOLD),
            TextNode(' with an ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC),
            TextNode(' word and a ', TextType.TEXT),
            TextNode('code block', TextType.CODE),
            TextNode(' and an ', TextType.TEXT),
            TextNode('obi wan image', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
            TextNode(' and a ', TextType.TEXT),
            TextNode('link', TextType.LINK, 'https://boot.dev')
        ]

        test_results = text_to_textnodes(text)
        self.assertEqual(expected_results, test_results)

    def test_textToNodes_toHTML(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'
        expected_results = [
            TextNode('This is ', TextType.TEXT),
            TextNode('text', TextType.BOLD),
            TextNode(' with an ', TextType.TEXT),
            TextNode('italic', TextType.ITALIC),
            TextNode(' word and a ', TextType.TEXT),
            TextNode('code block', TextType.CODE),
            TextNode(' and an ', TextType.TEXT),
            TextNode('obi wan image', TextType.IMAGE, 'https://i.imgur.com/fJRm4Vk.jpeg'),
            TextNode(' and a ', TextType.TEXT),
            TextNode('link', TextType.LINK, 'https://boot.dev')
        ]

        test_results = text_to_textnodes(text)
        # for node in test_results:
        #     print(text_node_to_html_node(node))
        self.assertEqual(expected_results, test_results)

    def test_splitnodes_unorderedLists(self):
        text = '* Item 1\n* Item 2\n* Item 3'

        test_results = list_to_textnodes(text, TextType.UNORDERED_LIST)
        expected_results = [
            LeafNode('li', 'Item 1'),
            LeafNode('li', 'Item 2'),
            LeafNode('li', 'Item 3')
        ]
        self.assertEqual(list(map(lambda x: x.to_html(), test_results)), list(map(lambda x: x.to_html(), expected_results)))
        
    def test_split_unorderedLists_toHtml(self):
        text = '* Item 1\n* Item 2\n* Item 3'

        test_results = list(list_to_textnodes(text, TextType.UNORDERED_LIST))
        expected_results = [
            LeafNode('li', 'Item 1'),
            LeafNode('li', 'Item 2'),
            LeafNode('li', 'Item 3')
        ]
        self.assertEqual(list(map(lambda x: x.to_html(), test_results)), list(map(lambda x: x.to_html(), expected_results)))
    # def test_textToNodes_blockquote(self):
    #     text = '> First sentance in quote\n> Second sentance in quote\n> Third sentance in quote\n'

    def test_split_unorderedLists_toHtml_withFormatting(self):
        text = '* Item 1 is an *apple*\n* Item 2\n* Item 3'

        test_results = list(list_to_textnodes(text, TextType.UNORDERED_LIST))
        expected_results = [
            LeafNode('li', 'Item 1 is an *apple*'),
            LeafNode('li', 'Item 2'),
            LeafNode('li', 'Item 3')
        ]
        
        list_to_textnodes(text, TextType.UNORDERED_LIST)
        # self.assertEqual(list(map(lambda x: x.to_html(), test_results)), list(map(lambda x: x.to_html(), expected_results)))