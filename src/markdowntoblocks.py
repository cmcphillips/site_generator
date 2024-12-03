import re

def markdown_to_blocks(text):
    
    # print(f'split: {re.sub(r' +\n', '\n', text).split('\n\n')}')    
    # print(f'filter: {list(filter(lambda x: x.strip() != '' and x!= '\n', re.sub(r' +\n +', '\n', text).split('\n\n')))}')
    
    blocks = list( 
        map(
            lambda y: ('\n').join(
                list(map(lambda x: x.strip(), y.split('\n')))
            ).lstrip('\n')
            , list(filter(lambda x: x.strip() != '' and x!= '\n', re.sub(r' +\n', '\n', text).split('\n\n')))
        )
    )
    return blocks

def block_to_block_type(block):
    '''
    Need to define:
    Paragraph
    Headings
    Code
    Quote
    Unordered Lists
    Ordered Lists
    '''

    # print(len(block.split('\n')))
    # len(list(filter(lambda x: x[0] == '-', list(filter(lambda y: y != '', block.split('\n'))))))



    # Headings
    if '#' in block:
        return f'Heading {block.count('#')}'
    
    # Code
    elif '```' in block:
        return 'Code'
    # Quote
    elif block[0] == '>':
        return 'Quote'
    # Unordered Lists
    elif len(list(filter(lambda x: x != '', block.split('\n')))) == len(list(filter(lambda x: x[0] == '*', list(filter(lambda y: y != '', block.split('\n')))))):
        return 'Unordered List'
    elif len(list(filter(lambda x: x != '', block.split('\n')))) == len(list(filter(lambda x: x[0] == '-', list(filter(lambda y: y != '', block.split('\n')))))):
        return 'Unordered List'
    # Ordered Lists
    elif re.findall(r'\d\.', block) == list(map(lambda x: x[:2], list(filter(lambda y: y != '', block.split('\n'))))):
        return 'Ordered List'
    # Paragraph
    else:
        return 'Paragraph'
