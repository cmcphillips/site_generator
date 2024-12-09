import re
from textnode import TextNode, TextType, text_node_to_html_node
from htmlnode import LeafNode, ParentNode
from splitnode import split_nodes_delimiter, split_nodes_link, split_nodes_image, split_list_nodes
# from htmlnode import LeafNode

def text_to_textnodes(text):
    '''
    Takes a text block and returns a list of TextNodes. Can delimite Code, Bold, Italic, Links and Images.
    '''
    text_node = [TextNode(text, TextType.TEXT)]

    text_node = split_nodes_delimiter(text_node, '`', TextType.CODE)
    text_node = split_nodes_delimiter(text_node, '**', TextType.BOLD)
    text_node = split_nodes_delimiter(text_node, '*', TextType.ITALIC)
    text_node = split_nodes_delimiter(text_node, '_', TextType.ITALIC)

    # text_node = split_list_nodes(text_node, '>', TextType.QUOTE)

    text_node = split_nodes_link(text_node)
    text_node = split_nodes_image(text_node)

    return text_node

# def quote_to_textnodes(text):
#     '''
#     Takes a text block from a QUOTE text type and returns a 
#     '''
#     pass


def list_to_textnodes(text, text_type):
    '''
    Takes a text block and returns a list of TextNodes for an Unordered or Ordered list.
    '''
    return split_list_nodes(text, text_type)

# def quote_to_textnodes(text, text_type):
#     pass

def text_to_children(text, tag, text_type):
    '''
    Takes a text, tag, and TextType and returns the appropriate LeafNode or ParentNode with all of it's associated nodes.
    '''
    # print(f'text_to_children called\ntext: {text}\ntag: {tag}\ntext_type: {text_type}\n')

    # Paragraph also include Images and Links
    if text_type == TextType.PARAGRAPH:
        return ParentNode(tag, list(map(lambda x: text_node_to_html_node(x), text_to_textnodes(text))))
    elif text_type == TextType.HEADER:
        return ParentNode(tag, list(map(lambda x: text_node_to_html_node(x), text_to_textnodes(re.sub('#{1,6} ', '', text)))))
    elif text_type == TextType.CODE:
        return ParentNode(tag, list(map(lambda x: text_node_to_html_node(x), text_to_textnodes(re.sub('```', '', text)))))
    elif text_type == TextType.QUOTE:
        return ParentNode(tag, list(map(lambda x: text_node_to_html_node(x), text_to_textnodes(re.sub('> *', '', text)))))
    elif text_type in(TextType.UNORDERED_LIST, TextType.ORDERED_LIST):
        return ParentNode(tag, list(map(lambda x: text_node_to_html_node(x), list_to_textnodes(text, text_type))))
    
    '''
    - handle code (call text to text nodes)
    - handle quote (similar to text?)
    '''
    pass