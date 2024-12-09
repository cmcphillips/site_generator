import unittest
from textnode import TextType
from htmlnode import LeafNode, ParentNode
from markdowntoblocks import markdown_to_blocks, block_to_block_type, markdown_to_html_node


class TestMarkdownToBlocks(unittest.TestCase):
    def test_markdownToBlocks(self):
        doc = '''# This is a heading

This is a paragraph of text. It has some **bold** and *italic* words inside of it.

* This is the first list item in a list block
* This is a list item   
* This is another list item   '''
        expected = [
            '# This is a heading', 
            'This is a paragraph of text. It has some **bold** and *italic* words inside of it.',
            '* This is the first list item in a list block\n* This is a list item\n* This is another list item'
        ]
        self.assertEqual(expected, markdown_to_blocks(doc))
        # print(doc)

        doc = '''# This is a heading

1. This is an ordered list
2. This is still an ordered list
3. This is the last item in the ordered list

* This is the first unordered list item
* This is the second unordered list item

```this is some code```

- This is the first unordered list item
- This is the second unordered list item'''
        expected = [
            '# This is a heading',
            '1. This is an ordered list\n2. This is still an ordered list\n3. This is the last item in the ordered list',
            '* This is the first unordered list item\n* This is the second unordered list item',
            '```this is some code```',
            '- This is the first unordered list item\n- This is the second unordered list item'
        ]
        self.assertEqual(expected, markdown_to_blocks(doc))
    
    def test_markdownToBlocks_variosEndingNewLines(self):
        doc = '''# This is a heading'''
        doc1 = '''# This is a heading\n'''
        doc2 = '''# This is a heading\n\n'''
        doc3 = '''# This is a heading\n\n\n'''
        doc4 = '''# This is a heading\n\n\n\n'''
        expected = ['# This is a heading']
        self.assertEqual(expected, markdown_to_blocks(doc))
        self.assertEqual(expected, markdown_to_blocks(doc1))
        self.assertEqual(expected, markdown_to_blocks(doc2))
        self.assertEqual(expected, markdown_to_blocks(doc3))
        self.assertEqual(expected, markdown_to_blocks(doc4))

    def test_blockToBlockType(self):
        doc = '''# This is a heading

1. This is an ordered list
2. This is still an ordered list
3. This is the last item in the ordered list

* This is the first unordered list item
* This is the second unordered list item

```this is some code```

- This is the first unordered list item
- This is the second unordered list item





'''
        
        blocks = markdown_to_blocks(doc)
        expected = [
            TextType.HEADER,
            TextType.ORDERED_LIST,
            TextType.UNORDERED_LIST,
            TextType.CODE,
            TextType.UNORDERED_LIST
        ]
        result = []
        # print(f'blocks: {blocks}')

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''# This is a heading

1. This is an ordered list
2. This is still an ordered list
3. This is the last item in the ordered list

* This is the first unordered list item
* This is the second unordered list item

```this is some code```

- This is the first unordered list item
- This is the second unordered list item
'''
        
        blocks = markdown_to_blocks(doc)
        expected = [
            TextType.HEADER,
            TextType.ORDERED_LIST,
            TextType.UNORDERED_LIST,
            TextType.CODE,
            TextType.UNORDERED_LIST
        ]
        result = []
        # print(f'blocks: {blocks}')

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)


        doc = '''# This is a heading

1. This is an ordered list
2. This is still an ordered list
3. This is the last item in the ordered list

* This is the first unordered list item
* This is the second unordered list item

```this is some code```

- This is the first unordered list item
- This is the second unordered list item'''
        
        blocks = markdown_to_blocks(doc)
        expected = [
            TextType.HEADER,
            TextType.ORDERED_LIST,
            TextType.UNORDERED_LIST,
            TextType.CODE,
            TextType.UNORDERED_LIST
        ]
        result = []
        # print(f'blocks: {blocks}')

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''# This is a heading

1. This is an ordered list     
2. This is still an ordered list
3. This is the last item in the ordered list

* This is the first unordered list item
* This is the second unordered list item

```this is some code```

> This is a quote

- This is the first unordered list item
- This is the second unordered list item'''
        
        blocks = markdown_to_blocks(doc)
        expected = [
            TextType.HEADER,
            TextType.ORDERED_LIST,
            TextType.UNORDERED_LIST,
            TextType.CODE,
            TextType.QUOTE,
            TextType.UNORDERED_LIST
        ]
        result = []
        # print(f'blocks: {blocks}')

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''# This is a heading

1. This is an ordered list     
2. This is still an ordered list
3. This is the last item in the ordered list

* This is the first unordered list item
* This is the second unordered list item

```this is some code```

> This is a quote
>
> This is the same quote

- This is the first unordered list item
- This is the second unordered list item'''
        
        blocks = markdown_to_blocks(doc)
        expected = [
            TextType.HEADER,
            TextType.ORDERED_LIST,
            TextType.UNORDERED_LIST,
            TextType.CODE,
            TextType.QUOTE,
            TextType.UNORDERED_LIST
        ]
        result = []
        # print(f'blocks: {blocks}')

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)


        # Testing Quotes
        doc = '''> This is a quote'''
        
        blocks = markdown_to_blocks(doc)
        expected = [TextType.QUOTE]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''> This is a quote
        '''
        
        blocks = markdown_to_blocks(doc)
        expected = [TextType.QUOTE]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
        > This is a quote    '''
        
        blocks = markdown_to_blocks(doc)
        expected = [TextType.QUOTE]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
        > This is a quote
        '''
        
        blocks = markdown_to_blocks(doc)
        expected = [TextType.QUOTE]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
        

        > This is a quote     
        
        '''
        
        blocks = markdown_to_blocks(doc)
        expected = [TextType.QUOTE]
        result = []

        # print(f'blocks: {blocks}')

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)
        
        doc = '''

> This is a quote     
    
> This is also a quote
'''
        
        blocks = markdown_to_blocks(doc)

        # print(f'blocks: {blocks}')
        expected = [TextType.QUOTE, TextType.QUOTE]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)


        doc = '''This is a paragraph

This is another paragraph
'''
        
        blocks = markdown_to_blocks(doc)

        # print(f'blocks: {blocks}')
        expected = [TextType.PARAGRAPH, TextType.PARAGRAPH]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
This is a paragraph
This is a part of the same paragraph

This is another paragraph
'''
        
        blocks = markdown_to_blocks(doc)

        # print(f'blocks: {blocks}')
        expected = [TextType.PARAGRAPH, TextType.PARAGRAPH]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
This is a paragraph
This is a part of the same paragraph
* this is bold*
* so is this* but not this

This is another paragraph
> will this break things? (nope)

Lets add an email mcphillips@duck.com
'''
        
        blocks = markdown_to_blocks(doc)

        # print(f'blocks: {blocks}')
        expected = [TextType.PARAGRAPH, TextType.PARAGRAPH, TextType.PARAGRAPH]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)


        doc = '''

> This is a quote
But not really, it's a paragraph. 
Or a Chimera.
    
> This is also a quote
'''
        
        blocks = markdown_to_blocks(doc)

        # print(f'blocks: {blocks}')
        expected = [TextType.PARAGRAPH, TextType.QUOTE]
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)


    def test_markdownToHtmlNode(self): #WIP
        doc = '''# This is a heading

This is a paragraph.
This is a second sentance in the paragraph.
This is the third sentance in the paragraph.
This is the last sentance in the paragraph.

1. This is an ordered list     
2. This is still an ordered list
3. This is the last item in the ordered list

* This is the first unordered list item
* This is the second unordered list item

```this is some code```

> This is a quote
>
> This is the same quote

- This is the first unordered list item again
- This is the second unordered list item again

![obi wan image](https://i.imgur.com/fJRm4Vk.jpeg)

[link](https://boot.dev)
'''
        expected_result =  ParentNode('div', [
            ParentNode('h1', [LeafNode(None, 'This is a heading')]), 
            ParentNode('p', [LeafNode(None, '''This is a paragraph.
This is a second sentance in the paragraph.
This is the third sentance in the paragraph.
This is the last sentance in the paragraph.''')]),
            ParentNode('ol', [LeafNode('li', 'This is an ordered list'),
                            LeafNode('li', 'This is still an ordered list'),
                            LeafNode('li', 'This is the last item in the ordered list')
                            ]),
            ParentNode('ul', [LeafNode('li', 'This is the first unordered list item'),
                              LeafNode('li', 'This is the second unordered list item')
                              ]),
            ParentNode('code', [LeafNode(None, 'this is some code')]),
            ParentNode('blockquote', [LeafNode(None, '''This is a quote

This is the same quote''')]),
            ParentNode('ul', [LeafNode('li', 'This is the first unordered list item again'),
                              LeafNode('li', 'This is the second unordered list item again')
                              ]),
            ParentNode('p', [LeafNode('img', '', {'src': 'https://i.imgur.com/fJRm4Vk.jpeg', 'alt': 'obi wan image'})]),
            ParentNode('p', [LeafNode('a', 'link', {'href': 'https://boot.dev'})])
        ])
        result = markdown_to_html_node(doc)
        # for i in result:
        #     print(f'result: {i}')
        # print(list(map(lambda x: x.to_html(), result)))
        # print(list(map(lambda x: x.to_html(), expected_result)))
        self.assertEqual(list(map(lambda x: x.to_html(), [expected_result])), list(map(lambda x: x.to_html(), [result])))

        text = result.to_html()
        print(repr(text))