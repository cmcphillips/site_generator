import unittest
from extractlink import extract_markdown_images, extract_markdown_links

class TestImageExtract(unittest.TestCase):
    def test_imageExtract(self):
        text = 'This is text with a ![rick roll](https://i.imgur.com/aKaOqIh.gif) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        expected_result = [('rick roll', 'https://i.imgur.com/aKaOqIh.gif'), ('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        # print(extract_markdown_images(text))
        self.assertEqual(extract_markdown_images(text), expected_result)

        text = 'This is text with a [to boot dev](https://www.boot.dev) and ![obi wan](https://i.imgur.com/fJRm4Vk.jpeg)'
        expected_result = [('obi wan', 'https://i.imgur.com/fJRm4Vk.jpeg')]
        # print(extract_markdown_images(text))
        self.assertEqual(extract_markdown_images(text), expected_result)


    def test_linkExtract(self):
        text = 'This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)'
        expected_result = [('to boot dev', 'https://www.boot.dev'), ('to youtube', 'https://www.youtube.com/@bootdotdev')]
        # print(extract_markdown_links(text))
        self.assertEqual(extract_markdown_links(text), expected_result)


        text = 'This is text with a link ![rick roll](https://i.imgur.com/aKaOqIh.gif) and [to youtube](https://www.youtube.com/@bootdotdev)'
        expected_result = [('to youtube', 'https://www.youtube.com/@bootdotdev')]
        # print(extract_markdown_links(text))
        self.assertEqual(extract_markdown_links(text), expected_result)