from enum import Enum
from functools import reduce

class HTMLNode():
    
    def __init__(self, tag = None, value = None, children = None, props = None):
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
        return (f'HTMLNode\ntag: {self.tag}\nvalue: {self.value}\nchildren: {self.children}\nprops: {self.props}')
    

class LeafNode(HTMLNode):
    def __init__(self, tag, value, props = None):
        super().__init__(tag, value, None, props)

    # Handle Bold, Italic, Paragraph, Code
    def to_html_bipcode(self, tag, value):
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
                return self.to_html_bipcode(self.tag, self.value)
            elif self.tag =='code':
                return self.to_html_bipcode(self.tag, self.value)
            elif self.tag =='>':
                return self.to_html_bipcode('blockquote', self.value)
            elif self.tag == 'a':
                return self.to_html_link(self.value, self.props_to_html())
            elif self.tag == 'img':
                return f'![{self.props['alt']}]({self.props['src']})'
        
class ParentNode(HTMLNode):
    def __init__(self, tag, children, props = None):
        super().__init__(tag, None, children, props)

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

