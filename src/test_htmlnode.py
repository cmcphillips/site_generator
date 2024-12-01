import unittest
from htmlnode import HTMLNode, LeafNode

class TestHTMLNode(unittest.TestCase):
    def test_HTMLNode(self):
        htmlNode = HTMLNode('tag', 'value', 'children', {'href': 'www.google.com', 'target': '_blank'})
        self.assertEqual(' href="www.google.com" target="_blank"', htmlNode.props_to_html())

        # Check that nothing can be passed into an HTMLNode
        htmlNodeNone = HTMLNode()
        self.assertEqual('', htmlNodeNone.props_to_html())

        # Check that we can only provide the props
        htmlNodePropsOnly = HTMLNode(props = {'href': 'www.gmail.com', 'target': 'blank'})
        self.assertEqual(' href="www.gmail.com" target="blank"', htmlNodePropsOnly.props_to_html())

    def test_LeafNode(self):
        leafNode = LeafNode('p', 'This is a paragraph of text.')
        print(f'leafNode: {leafNode.to_html()}')
        
        leafNode2 = LeafNode('a', 'Click me!', props={'href': 'https://www.google.com'})
        print(f'leafNode2: {leafNode2.to_html()}')



if __name__ == '__main__':
    unittest.main()