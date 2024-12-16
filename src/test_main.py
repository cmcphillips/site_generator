import unittest
from main import extract_title
import re

class TestMain(unittest.TestCase):
    
    # Test simple case
    def test_extractTitle(self):
        markdown = '# Title of Markdown'
        expected = 'Title of Markdown'
        result = extract_title(markdown)
        self.assertEqual(result, expected)

    # Test multiple lines
    def test_extractTitle(self):
        markdown = '# Title of Markdown\n\nParagraph line\n'
        expected = 'Title of Markdown'
        result = extract_title(markdown)
        self.assertEqual(result, expected)

    # Test leading and trailing spaces
    def test_extractTitle(self):
        markdown = '#     Title of Markdown    \n\nParagraph line\n'
        expected = 'Title of Markdown'
        result = extract_title(markdown)
        self.assertEqual(result, expected)
    
    # Test bold instead of Header 1 (Not Equal)
    def test_extractTitle(self):
        markdown = '## Title of Markdown\n\nParagraph line\n'
        expected = 'Title of Markdown'
        result = extract_title(markdown)
        self.assertNotEqual(result, expected)

    # Test bold instead of Header 1 (Not Equal)
    def test_extractTitle(self):
        markdown = '## Title of Markdown\n\nParagraph line\n'
        expected = f'No title found in markdown. First line is: {markdown.split('\n')[0]}'
        # result = 
        with self.assertRaises(Exception) as cm:
            extract_title(markdown)
        self.assertTrue(f'No title found in markdown. First line is: {markdown.split('\n')[0]}' in str(cm.exception))

    # Test example .md file
    def test_extractTitle(self):
        markdown = '''# Tolkien Fan Club

**I like Tolkien**. Read my [first post here](/majesty) (sorry the link doesn't work yet)

'''
        expected = 'Tolkien Fan Club'
        #result = extract_title(markdown)

        # print(markdown.split('\n')[0])
        # print(re.findall('#(?<!##) .*', markdown.split('\n')[0]))
        # self.assertEqual(result, expected)