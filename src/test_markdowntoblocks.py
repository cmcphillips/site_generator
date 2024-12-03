import unittest
from markdowntoblocks import markdown_to_blocks, block_to_block_type

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
            'Heading 1',
            'Ordered List',
            'Unordered List',
            'Code',
            'Unordered List'
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
            'Heading 1',
            'Ordered List',
            'Unordered List',
            'Code',
            'Unordered List'
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
            'Heading 1',
            'Ordered List',
            'Unordered List',
            'Code',
            'Unordered List'
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
            'Heading 1',
            'Ordered List',
            'Unordered List',
            'Code',
            'Quote',
            'Unordered List'
        ]
        result = []
        # print(f'blocks: {blocks}')

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        # Testing Quotes
        doc = '''> This is a quote'''
        
        blocks = markdown_to_blocks(doc)
        expected = ['Quote']
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''> This is a quote
        '''
        
        blocks = markdown_to_blocks(doc)
        expected = ['Quote']
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
        > This is a quote    '''
        
        blocks = markdown_to_blocks(doc)
        expected = ['Quote']
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
        > This is a quote
        '''
        
        blocks = markdown_to_blocks(doc)
        expected = ['Quote']
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)

        doc = '''
        

        > This is a quote     
        
        '''
        
        blocks = markdown_to_blocks(doc)
        expected = ['Quote']
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
        expected = ['Quote', 'Quote']
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)


        doc = '''This is a paragraph

This is another paragraph
'''
        
        blocks = markdown_to_blocks(doc)

        # print(f'blocks: {blocks}')
        expected = ['Paragraph', 'Paragraph']
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
        expected = ['Paragraph', 'Paragraph']
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
        expected = ['Paragraph', 'Paragraph', 'Paragraph']
        result = []

        for block in blocks:
            result.append(block_to_block_type(block))
        self.assertEqual(expected, result)


        