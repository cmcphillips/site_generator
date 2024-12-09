import re
from htmlnode import ParentNode
from textnode import TextType
from texttonodes import text_to_children

def markdown_to_blocks(text):
    '''
    Takes a markdown document and returns a list of text/blocks.
    '''
    # print(f'split: {re.sub(r' +\n', '\n', text).split('\n\n')}')    
    # print(f'filter: {list(filter(lambda x: x.strip() != '' and x!= '\n', re.sub(r' +\n +', '\n', text).split('\n\n')))}')
    
    blocks = list( 
        map(
            lambda y: ('\n').join(
                list(map(lambda x: x.strip(), y.split('\n')))
            ).strip('\n') # Updated to get rid of the first '\n' from the ('\n').join and any following ones
            , list(filter(lambda x: x.strip() != '' and x!= '\n', re.sub(r' +\n', '\n', text).split('\n\n')))
        )
    )
    return blocks

def block_to_block_type(block):
    '''
    Takes a block (text) and returns the type of block identified from the text.
    '''

    # print(len(block.split('\n')))
    # len(list(filter(lambda x: x[0] == '-', list(filter(lambda y: y != '', block.split('\n'))))))

    # Headings
    if '#' in block:
        return TextType.HEADER #f'Heading {block.count('#')}'
    
    # Code
    elif '```' in block:
        return TextType.CODE
    # Quote
    # elif block[0] == '>': # Old elif  
    elif len(list(filter(lambda x: x != '', block.split('\n')))) == len(list(filter(lambda x: x[0] == '>', list(filter(lambda y: y != '', block.split('\n')))))): # new elif
        return TextType.QUOTE
    # Unordered Lists
    elif len(list(filter(lambda x: x != '', block.split('\n')))) == len(list(filter(lambda x: x[0] == '*', list(filter(lambda y: y != '', block.split('\n')))))):
        return TextType.UNORDERED_LIST
    elif len(list(filter(lambda x: x != '', block.split('\n')))) == len(list(filter(lambda x: x[0] == '-', list(filter(lambda y: y != '', block.split('\n')))))):
        return TextType.UNORDERED_LIST
    # Ordered Lists
    elif re.findall(r'\d\.', block) == list(map(lambda x: x[:2], list(filter(lambda y: y != '', block.split('\n'))))):
        return TextType.ORDERED_LIST
    # Paragraph
    else:
        return TextType.PARAGRAPH

def get_block_type_html_tag(block_type, block = None):
    '''
    Takes a block_type and returns the corresponding HTML tag.
    '''
    if block_type == TextType.HEADER:
        return f'h{block.count('#')}'
    elif block_type == TextType.CODE:
        return 'code'
    elif block_type == TextType.UNORDERED_LIST:
        return 'ul'
    elif block_type == TextType.ORDERED_LIST:
        return 'ol'
    elif block_type == TextType.QUOTE:
        return 'blockquote'
    elif block_type == TextType.PARAGRAPH:
        return 'p'
    else:
        raise ValueError(f'Unexpected block_type: {block_type}')

def markdown_to_html_node(markdown):
    '''
    WIP: Takes a markdown document and returns an HTML Node representation.
    '''
    # Get a list of text blocks from the markdown
    markdown_blocks = markdown_to_blocks(markdown)

    # Get the block type of each block
    # Create a list of tuples: (block, block_type)
    markdown_blocks_and_types = []
    for block in markdown_blocks:
        markdown_blocks_and_types.append((block, block_to_block_type(block)))
    
    # return markdown_blocks_and_types

    markdown_nodes_list = []
    for block_text, block_type in markdown_blocks_and_types:
        markdown_nodes_list.append(text_to_children(block_text, get_block_type_html_tag(block_type, block_text), block_type))

    html_node = ParentNode('div', markdown_nodes_list)
    
    #return markdown_blocks_and_types
    return html_node


