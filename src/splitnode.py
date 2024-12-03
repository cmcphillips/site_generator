from textnode import TextNode, TextType
from extractlink import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        for i in range(0, len(node.text.split(delimiter))):
            if i % 2 == 0:
                new_nodes.append(TextNode(node.text.split(delimiter)[i], node.text_type))
            else:
                new_nodes.append(TextNode(node.text.split(delimiter)[i], text_type))

    return new_nodes

def split_text_from_images(text, images):
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
