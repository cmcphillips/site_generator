from enum import Enum
from functools import reduce

class HTMLNode():
    
    def __init__(self, tag = None, value = None, children = None, props = None):
        # self.class_name = 'HTML'
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
        
    def to_html(self):
        raise NotImplementedError()
    
    def props_to_html(self):
        if self.props is None:
            return ''
        else:
            return reduce((lambda x, y: x + f' {y[0]}="{y[1]}"'), list(self.props.items()), '')
        
    def __repr__(self):
        string = f'\n\n{self.__class__.__name__}'
        string += f'\ntag: {self.tag}' if self.tag is not None else ''
        string += f'\nvalue: {self.value}' if self.value is not None else ''
        string += f'\nchildren: {self.children}' if self.children is not None else ''
        string += f'\nprops: {self.props}' if self.props is not None else ''
        return (string)
        # return (f'HTMLNode\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}')

    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)
        # self.class_name = 'Leaf'

    # Handle Bold, Italic, Paragraph, Code
    def to_html_singleTag(self, tag, value):
        return f'<{tag}>{value}</{tag}>'
    
    def to_html_link(self, value, props):
        return f'<a{props}>{value}</a>'
    
    def to_html(self):
        if self.value is None:
            raise ValueError('LeafNode value cannot be None')
        if self.tag is None:
            return self.value
        else:
            if len(self.tag) == 1 and self.tag in 'bip':
                return self.to_html_singleTag(self.tag, self.value)
            elif self.tag =='code':
                return self.to_html_singleTag(self.tag, self.value)
            elif self.tag =='blockquote':
                return self.to_html_singleTag(self.tag, self.value)
            elif self.tag == 'a':
                return self.to_html_link(self.value, self.props_to_html())
            elif self.tag == 'img':
                return f'![{self.props['alt']}]({self.props['src']})'
            elif self.tag == 'li':
                return self.to_html_singleTag('li', self.value)
            # elif self.tag[0] == 'h': --might not need
            #     return self.to_html_singleTag(self.tag, self.value)
            else:
                raise ValueError(f'{self.tag} is not handled in to_html function.')
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)
        # self.class_name = 'Leaf'

    def to_html(self):
        if self.tag is None:
            raise ValueError('ParentNode tag cannot be None')
        elif self.children is None:
            raise ValueError('ParentNode children cannot be None')
        else:
            children_html = ''
            for child in self.children:
                children_html += child.to_html()
            return f'<{self.tag}{self.props_to_html()}>{children_html}</{self.tag}>'

