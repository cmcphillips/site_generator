import re
from textnode import TextNode, TextType
from extractlink import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    '''
    Takes a list of TextNodes, a delimiter, and text_type for the delimiter, and returns a list of nodes with the provided delimiter and text_type separated out.
    '''
    new_nodes = []
    for node in old_nodes:
        for i in range(0, len(node.text.split(delimiter))):
            if i % 2 == 0:
                new_nodes.append(TextNode(node.text.split(delimiter)[i], node.text_type))
            else:
                new_nodes.append(TextNode(node.text.split(delimiter)[i], text_type))

    return new_nodes

def split_text_from_images(text, images):
    '''
    Takes a text string and a list of a list of image-tuples and returns a list of the text string with the image seperator(s) removed.
    '''
    new_text = []
    if len(images) == 0:
        return [text]#text.split(f'![{images[0][0]}]({images[0][1]})')[0]
    else:
        # print(new_text)
        new_text.append(text.split(f'![{images[0][0]}]({images[0][1]})')[0])
        # print(new_text)
        # print(f'passed on text: {text.split(f'![{images[0][0]}]({images[0][1]})')[1]}')
        new_text += split_text_from_images(text.split(f'![{images[0][0]}]({images[0][1]})')[1], images[1:])
        # new_text.append(
        # print(new_text)
    return new_text

def split_text_from_links(text, links):
    '''
    Takes a text string and a list of a list of link-tuples and returns a list of the text string with the link seperator(s) removed.
    '''
    new_text = []
    if len(links) == 0:
        return [text]#text.split(f'![{images[0][0]}]({images[0][1]})')[0]
    else:
        # print(new_text)
        new_text.append(text.split(f'[{links[0][0]}]({links[0][1]})')[0])
        # print(new_text)
        # print(f'passed on text: {text.split(f'![{images[0][0]}]({images[0][1]})')[1]}')
        new_text += split_text_from_links(text.split(f'[{links[0][0]}]({links[0][1]})')[1], links[1:])
        # new_text.append(
        # print(new_text)
    return new_text

def split_nodes_image(old_nodes):
    '''
    Takes a list of TextNodes and returns a list of TextNodes with the images broken out.
    '''
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        # print(f'node_text: {node_text}')
        images = extract_markdown_images(node.text)
        # print(f'images: {images}')
        if images != []:
            text_separated = split_text_from_images(node_text, images)

            for i in range(0, (len(text_separated) + len(images))): # Should always be an odd number with text having 1 more than images
                if i % 2 == 0 and text_separated[int(i/2)] != '':
                    new_nodes.append(TextNode(text_separated[int(i/2)], TextType.TEXT))
                elif i % 2 == 0 and text_separated[int(i/2)] == '':
                    continue 
                else:
                    new_nodes.append(TextNode(images[int((i-1)/2)][0], TextType.IMAGE, images[int((i-1)/2)][1]))
        else:
            new_nodes.append(node)

    return new_nodes
            # This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)


def split_nodes_link(old_nodes):
    '''
    Takes a list of TextNodes and returns a list of TextNodes with the links broken out.
    '''
    new_nodes = []
    for node in old_nodes:
        node_text = node.text
        # print(f'node_text: {node_text}')
        links = extract_markdown_links(node.text)
        # print(f'links: {links}')
        if links != []:
            text_separated = split_text_from_links(node_text, links)
            # print(f'text separated: {text_separated}')
            for i in range(0, (len(text_separated) + len(links))): # Should always be an odd number with text having 1 more than links
                if i % 2 == 0 and text_separated[int(i/2)] != '':
                    new_nodes.append(TextNode(text_separated[int(i/2)], TextType.TEXT))
                elif i % 2 == 0 and text_separated[int(i/2)] == '':
                    continue
                else:
                    new_nodes.append(TextNode(links[int((i-1)/2)][0], TextType.LINK, links[int((i-1)/2)][1]))
        else:
            new_nodes.append(node)

    return new_nodes
            # This is text with a link [to boot dev](https://www.boot.dev) and [to youtube](https://www.youtube.com/@bootdotdev)

def split_list_nodes(text, text_type):
    '''
    Takes a text and text_type of Ordered or Unordered List and returns a list of TextNodes for each list item.
    '''
    new_nodes = []
    if text_type == TextType.ORDERED_LIST:
        # re.findall(r'\d\.', block) == list(map(lambda x: re.sub(r'\d\. *', x), list(filter(lambda y: y != '', block.split('\n'))))):
        # list_items = list(map(lambda x: re.sub(r'\d\. *', x), list(filter(lambda y: y != '', text.split('\n')))))
        list_items = list(map(lambda x: re.sub(r'\d\. *', '', x), text.split('\n')))#, list(filter(lambda y: y != '', text.split('\n')))))
        # return 'Ordered List'
        
    elif text_type == TextType.UNORDERED_LIST:
        if len(list(filter(lambda x: x != '', text.split('\n')))) == len(list(filter(lambda x: x[0] == '*', list(filter(lambda y: y != '', text.split('\n')))))):
            list_items = list(map(lambda x: re.sub(r'\* *', '', x), list(filter(lambda y: y != '', text.split('\n')))))#         x[0] == '*', list(filter(lambda y: y != '', text.split('\n')))))

        elif len(list(filter(lambda x: x != '', text.split('\n')))) == len(list(filter(lambda x: x[0] == '-', list(filter(lambda y: y != '', text.split('\n')))))):
            list_items = list(map(lambda x: re.sub(r'- *', '', x), list(filter(lambda y: y != '', text.split('\n')))))#         x[0] == '*', list(filter(lambda y: y != '', text.split('\n')))))
        
    else:
        raise ValueError(f'Unexpected text_type: {text_type} received by text_to_list_nodes.')

    for i in list_items: 
        new_nodes.append(TextNode(i, text_type))

    return new_nodes

# def split_quotes_delimiter(old_nodes, text_type):
#     '''
#     Takes a list of QUOTE nodes and returns a list of nodes for any nested quotes
#     '''

#     new_nodes = []
#     for node in old_nodes:
#         if len(node.text.split('>>')) > 1:
            
#         else:
#             return node.text

#         for i in range(0, len(node.text.split('>>'))):
#             if i % 2 == 0:
#                 new_nodes.append(TextNode(node.text.split(delimiter)[i], node.text_type))
#             else:
#                 new_nodes.append(TextNode(node.text.split(delimiter)[i], text_type))

#     return new_nodes