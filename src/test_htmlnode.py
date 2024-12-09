import unittest
from htmlnode import HTMLNode, LeafNode, ParentNode

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
        # print(f'leafNode: {leafNode.to_html()}')
        self.assertEqual('<p>This is a paragraph of text.</p>', leafNode.to_html())
        
        # Test Link type LeafNode
        leafNode2 = LeafNode('a', 'Click me!', props={'href': 'https://www.google.com'})
        self.assertEqual('<a href="https://www.google.com">Click me!</a>', leafNode2.to_html())

        # Test Image type LeafNode
        leaf_node = LeafNode('img', '', {'src': 'image_link.com', 'alt': 'Image text'})
        self.assertEqual('![Image text](image_link.com)', leaf_node.to_html())

    # Test that a LeafNode with value = None will raise a ValueError
    def test_LeafNode_None(self):
        leafNode = LeafNode('p', None)
        with self.assertRaises(ValueError):
            leafNode.to_html()

    def test_ParentNode(self):
        parent_node = ParentNode('p',  [
            LeafNode('b', 'Bold text'),
            LeafNode(None, 'Normal text'),
            LeafNode('i', 'italic text'),
            LeafNode(None, 'Normal text'),
            ],
        )
        #print(parent_node.to_html())
        self.assertEqual('<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>', parent_node.to_html())

        parent_node = ParentNode('p',  [
            LeafNode('b', 'Bold text'),
            LeafNode(None, 'Normal text'),
            LeafNode('i', 'italic text'),
            LeafNode(None, 'Normal text'),
            ParentNode('b', [
                LeafNode('code', 'code text'),
                LeafNode(None, 'Normal text')
                ],
            )
            ],
        )
        # print(parent_node.to_html())
        self.assertEqual('<p><b>Bold text</b>Normal text<i>italic text</i>Normal text<b><code>code text</code>Normal text</b></p>', parent_node.to_html())

        parent_node = ParentNode('i', [
            ParentNode('b', [
                ParentNode('p', [
                    LeafNode('code', 'code text')
                    ],
                )
                ],
            )
            ],
        )

        self.assertEqual('<i><b><p><code>code text</code></p></b></i>', parent_node.to_html())

if __name__ == '__main__':
    unittest.main()