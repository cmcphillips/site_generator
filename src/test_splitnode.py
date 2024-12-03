import unittest
from splitnode import split_nodes_delimiter, split_nodes_image, split_nodes_link
from textnode import TextNode, TextType

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