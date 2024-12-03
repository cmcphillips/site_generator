from textnode import TextNode, TextType
from splitnode import split_nodes_delimiter, split_nodes_link, split_nodes_image

def text_to_textnodes(text):
    text_node = [TextNode(text, TextType.TEXT)]

    text_node = split_nodes_delimiter(text_node, '`', TextType.CODE)
    text_node = split_nodes_delimiter(text_node, '**', TextType.BOLD)
    text_node = split_nodes_delimiter(text_node, '*', TextType.ITALIC)
    text_node = split_nodes_delimiter(text_node, '_', TextType.ITALIC)

    # text_node = split_nodes_delimiter([text_node], '>', TextType.QUOTE)
    # text_node = split_nodes_delimiter([text_node], '`', TextType.CODE)

    text_node = split_nodes_link(text_node)
    text_node = split_nodes_image(text_node)

    return text_node