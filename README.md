# site_generator


## Architecture

1. Break the Markdown document into TextNodes
2. Further breakdown the TextNodes to spit out links, italics, bold, images.
    e.g.
        Paragraph TextNode => List of single TextNode
        Paragraph TextNode => List of TextNodes of text, bold, italic

3. Convert the TextNodes into Parent and Leaf Nodes
4. Put all the nodes in a parent 'div' node

## Known Issues
- newlines in paragraphs are not handeled the way I initially thought. I should either remove the newlines from paragrpahs or make them each their own paragraph.