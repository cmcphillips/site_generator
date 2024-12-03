import unittest
from texttonodes import text_to_textnodes

class TestTextToNodes(unittest.TestCase):
    def test_textToNodes(self):
        text = 'This is **text** with an *italic* word and a `code block` and an ![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg) and a [link](https://boot.dev)'

        text_nodes = text_to_textnodes(text)
        # print('\nText Nodes:')
        # for i in text_nodes:
        #     print(i)

