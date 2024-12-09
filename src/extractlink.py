import re

def extract_markdown_images(text):
    '''
    Takes a text string and returns a list of tuples of image-src and image-url
    '''
    return re.findall(r'!\[(.*?)\]\((.*?\.com.*?)\)', text)

def extract_markdown_links(text):
    '''
    Takes a text string and returns a list of tuples of link-string and link-url
    '''
    return re.findall(r'(?<!!)\[(.*?)\]\((.*?)\)', text)