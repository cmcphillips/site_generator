from enum import Enum
from htmlnode import LeafNode, ParentNode
import re

class TextType(Enum):
    TEXT = 'text'
    PARAGRAPH = 'paragraph'
    HEADER = 'header'
    BOLD = 'bold'
    ITALIC = 'italic'
    LINK = 'link'
    IMAGE = 'image'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'
    QUOTE = 'quote'
    CODE = 'code'

class TextNode():
    def __init__(self, text, text_type, url = None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, text_node):
        if self.text == text_node.text and self.text_type == text_node.text_type and self.url == text_node.url:
            return True
        else:
            return False

    def __repr__(self):
        if self.url is None:
            return (f'TextNode("{self.text}", {self.text_type})')
        else:
            return (f'TextNode("{self.text}", {self.text_type}, {self.url})')
    
def text_node_to_html_node(text_node):
    '''
    Takes a TextNode and returns a LeafNode corresponding to the TextNode.text_type
    '''
    if text_node.text_type == TextType.TEXT:
        return LeafNode(None, text_node.text)
    elif text_node.text_type == TextType.PARAGRAPH:
        return LeafNode('p', text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode('b', text_node.text)
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode('i', text_node.text)
    elif text_node.text_type == TextType.LINK:
        return LeafNode('a', text_node.text, {'href': text_node.url})
    elif text_node.text_type == TextType.IMAGE:
        return LeafNode('img', '', {'src': text_node.url, 'alt': text_node.text})
    elif text_node.text_type == TextType.UNORDERED_LIST:
        return LeafNode('li', text_node.text)
        # raise NotImplemented('TextNode to Unordered Lists is not implemented')
    elif text_node.text_type == TextType.ORDERED_LIST:
        return LeafNode('li', text_node.text) #old way
        # return ParentNode('li', list(map(lambda x: text_node_to_html_node(x), text_to_textnodes(text_node.text)))) #new attempt
    elif text_node.text_type == TextType.QUOTE:
        # return LeafNode('blockquote', re.sub('> *', '', text_node.text))
        return ParentNode('blockquote', [LeafNode(None, re.sub('> *', '', text_node.text))])
        # raise NotImplemented('TextNode to Quote is not implemented')
    elif text_node.text_type == TextType.CODE:
        return LeafNode('code', text_node.text)
    else:
        raise Exception(f'Cannot convert TextNode of type {text_node.text_type}')
     
