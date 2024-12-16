from textnode import *
import os, shutil
import re
from markdowntoblocks import markdown_to_html_node

def copy_files_to_target(source, destination):
    if os.path.isfile(source):
        # print(f'Copying {source} to {destination}')
        shutil.copy(source, destination)
    else:
        for s, d in list(map(lambda p: (os.path.join(source, p), os.path.join(destination, p)), os.listdir(source))):
            if os.path.isdir(s) and not os.path.isdir(d):
                os.mkdir(d)
            copy_files_to_target(s, d)

def refresh_public_directory():
    '''
    Deletes all files & folders in the ./public directory and copies all files & folder from ./static into the ./public directory.
    '''
    source_directory = './static'
    target_directory = './public'

    if os.path.exists(source_directory):
        pass
    else:
        raise Exception(f'Source directory({source_directory}) does not exist.')
    
    if os.path.exists(target_directory):
        pass
    else:
        raise Exception(f'Target directory({target_directory}) does not exist.')

    # Delete everything in target directory

    for d in list(map(lambda p: os.path.join(target_directory, p), os.listdir(target_directory))):
        print(f'Deleting {d}')
        if os.path.isfile(d):
            os.remove(d)
        elif os.path.isdir(d):
            shutil.rmtree(d)
        else:
            raise Exception(f'Unexpected file type for path: {d}')

    # Recursively copy files from source to target
    copy_files_to_target(source_directory, target_directory)

def extract_title(markdown):
    '''
    Returns the title of the markdown document. Errors if no title is found.
    '''
    title = re.findall('#(?<!##) .*', markdown.split('\n')[0])

    if len(title) > 0:
        return title[0].replace('# ', '').strip(' ')
    else:
        raise Exception(f'No title found in markdown. First line is: {markdown.split('\n')[0]}')

def generate_page(from_path, template_path, dest_path):
    print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown = None
    template = None

    with open(from_path) as md:
        markdown = md.read()
    md.close()

    with open(template_path) as t:
        template = t.read()
    t.close()

    # Generate an HTML node from markdown
    md_html = markdown_to_html_node(markdown)
    title = extract_title(markdown)

    # Replace title and content
    template = template.replace("{{ Title }}", title).replace("{{ Content }}", md_html.to_html())

    print(f'basename: {os.path.basename(from_path)}')
    # Save file
    with open(os.path.join(os.path.dirname(dest_path), f'{os.path.basename(from_path).replace('.md', '.html')}'), 'w') as s:
        s.write(template)
    s.close()
    
def generate_content(from_path, template_path, dest_path):
    
    print(f'from_path: {from_path}\n')
    print(f'from_path is file?: {os.path.isfile(from_path)}\n')

    if os.path.isfile(from_path):
        generate_page(from_path, template_path, dest_path)
    else:
        for f, d in list(map(lambda p: (os.path.join(from_path, p), os.path.join(dest_path, p)), os.listdir(from_path))):
            if os.path.isdir(f) and not os.path.isdir(d):
                print(f'Creating directory: {d}')
                os.mkdir(d)
            print(f'Calling generate_content with:\nfrom_path: {f}\ndest_path: {d}\n\n')
            generate_content(f, template_path, d)

def main():
    
    refresh_public_directory()
    generate_content('./content', './template.html', './public')
    
if __name__ == "__main__":
    main()