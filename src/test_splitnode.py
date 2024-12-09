import unittest
from htmlnode import LeafNode
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link, split_list_nodes
from textnode import TextNode, TextType, text_node_to_html_node

class TestSplitNode(unittest.TestCase):
    def test_spit_node(self):
        # Test text node doesn't split when no code exists but code split is attempted
        node = TextNode('This is normal text', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '`', TextType.CODE)
        expected_node = [TextNode('This is normal text', TextType.TEXT)]
        self.assertEqual(new_node, expected_node)

        # Test text node doesn't split when no code exists but code split is attempted
        node = TextNode('This is normal text with `code text` inside', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '`', TextType.CODE)
        expected_node = [
            TextNode('This is normal text with ', TextType.TEXT),
            TextNode('code text', TextType.CODE),
            TextNode(' inside', TextType.TEXT)]
        self.assertEqual(new_node, expected_node)

        # Test text node splits when code exists and code split is attempted
        node = TextNode('This is normal text with `code text` inside and at the end there is `code text again`', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '`', TextType.CODE)
        expected_node = [
            TextNode('This is normal text with ', TextType.TEXT),
            TextNode('code text', TextType.CODE),
            TextNode(' inside and at the end there is ', TextType.TEXT),
            TextNode('code text again', TextType.CODE),
            TextNode('', TextType.TEXT)
        ]
        self.assertEqual(new_node, expected_node)


        # Test text node splits when code exists in more than 1 spot and code split is attempted
        node = TextNode('This is normal text with `code text` inside and at the end there is `code text again`', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '`', TextType.CODE)
        expected_node = [
            TextNode('This is normal text with ', TextType.TEXT),
            TextNode('code text', TextType.CODE),
            TextNode(' inside and at the end there is ', TextType.TEXT),
            TextNode('code text again', TextType.CODE),
            TextNode('', TextType.TEXT)
        ]
        self.assertEqual(new_node, expected_node)

        # Test text node splits when italic exists and italic split is attempted
        node = TextNode('This contains *italic text*', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '*', TextType.ITALIC)
        expected_node = [
                TextNode('This contains ', TextType.TEXT),
                TextNode('italic text', TextType.ITALIC),
                TextNode('', TextType.TEXT)
            ]
        self.assertEqual(new_node, expected_node)

        # Test text node splits when italic and code exists and italic and code split is attempted
        node = TextNode('This contains *italic text* and `code text`', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '*', TextType.ITALIC)
        new_node = split_nodes_delimiter(new_node, '`', TextType.CODE)
        expected_node = [
                TextNode('This contains ', TextType.TEXT),
                TextNode('italic text', TextType.ITALIC),
                TextNode(' and ', TextType.TEXT),
                TextNode('code text', TextType.CODE),
                TextNode('', TextType.TEXT)
            ]
        self.assertEqual(new_node, expected_node)


        # Test text node splits when code exists inside italic 
        node = TextNode('This contains *italic text with `code text` inside*', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '*', TextType.ITALIC)
        new_node = split_nodes_delimiter(new_node, '`', TextType.CODE)
        expected_node = [
                TextNode('This contains ', TextType.TEXT),
                TextNode('italic text with ', TextType.ITALIC),
                TextNode('code text', TextType.CODE),
                TextNode(' inside', TextType.ITALIC),
                TextNode('', TextType.TEXT)
            ]
        self.assertEqual(new_node, expected_node)

        # Test text node splits when code exists inside italic and both end at same time
        node = TextNode('This contains *italic text with `code text`*', TextType.TEXT)
        new_node = split_nodes_delimiter([node], '*', TextType.ITALIC)
        new_node = split_nodes_delimiter(new_node, '`', TextType.CODE)
        expected_node = [
                TextNode('This contains ', TextType.TEXT),
                TextNode('italic text with ', TextType.ITALIC),
                TextNode('code text', TextType.CODE),
                TextNode('', TextType.ITALIC),
                TextNode('', TextType.TEXT)
            ]
        self.assertEqual(new_node, expected_node)

    def test_solo_link(self):
        new_node = [TextNode('[to boot dev](https://www.boot.dev)', TextType.TEXT)]
        expected_result = TextNode('to boot dev', TextType.LINK, 'https://www.boot.dev')
        self.assertEqual(split_nodes_link(new_node)[0], expected_result)

    def test_textSplit(self):
        node = [TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', TextType.TEXT)]
        # print(f'test split: {split_nodes_image(node)}')


        node = [TextNode('![gmail](https://gmail.com) This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', TextType.TEXT)]
        # print(f'test split: {split_nodes_image(node)}')


        node = [TextNode('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)]
        # print(f'test split: {split_nodes_link(node)}')


        node = [TextNode('This is text normal text', TextType.TEXT)]
        # print(f'test split: {split_nodes_link(node)}')

        node = [TextNode('This is text normal text', TextType.TEXT)]
        # print(f'test split: {split_nodes_image(node)}')


        node = [
            TextNode('This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)', TextType.TEXT),
            TextNode('This is text normal text', TextType.TEXT),
            TextNode('This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)', TextType.TEXT)
        ]
        # print('test split 1:')
        # for i in split_nodes_image(node):
        #     print(i)

        # print('test split 2:')
        # for i in split_nodes_link(node):
        #     print(i)
        # node2 = split_nodes_image(node)
        # # for i in node2:
        # #     print(i)

        # node3 = split_nodes_link(node2)
        # # for i in node3:
        #     print(i)

        node = [TextNode(" and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a ", TextType.TEXT)]
        # print(split_nodes_image(node))

    def test_splitnoes_unorderedLists(self):
        text = '* Item 1\n* Item 2\n* Item 3'

        test_results = split_list_nodes(text, TextType.UNORDERED_LIST)
        expected_results = [
            TextNode('Item 1', TextType.UNORDERED_LIST),
            TextNode('Item 2', TextType.UNORDERED_LIST),
            TextNode('Item 3', TextType.UNORDERED_LIST)
        ]
        self.assertEqual(expected_results, test_results)
        # print('\nText Nodes:')
        # for i in text_nodes:
        #     print(i) 
    def test_split_unorderedLists_toHtml(self):
        text = '* Item 1\n* Item 2\n* Item 3'

        test_results = list(map(lambda x: text_node_to_html_node(x), split_list_nodes(text, TextType.UNORDERED_LIST)))
        expected_results = [
            LeafNode('li', 'Item 1'),
            LeafNode('li', 'Item 2'),
            LeafNode('li', 'Item 3')
        ]
        self.assertEqual(list(map(lambda x: x.to_html(), test_results)), list(map(lambda x: x.to_html(), expected_results)))

    def test_textToNodes_orderedLists(self):
        text = '1. Item 1\n2. Item 2\n3. Item 3'

        test_results = list(map(lambda x: text_node_to_html_node(x), split_list_nodes(text, TextType.ORDERED_LIST)))
        expected_results = [
            LeafNode('li', 'Item 1'),
            LeafNode('li', 'Item 2'),
            LeafNode('li', 'Item 3')
        ]
        self.assertEqual(list(map(lambda x: x.to_html(), test_results)), list(map(lambda x: x.to_html(), expected_results)))


    # def test_split_nested_blockquote(self):
    #     text = '> Item 1\n> Item 2\n>>Item a\n>> Item b\n> Item 3'
    #     expected_results = [

    #     ]