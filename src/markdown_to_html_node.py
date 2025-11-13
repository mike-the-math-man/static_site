from markdown_to_blocks import markdown_to_blocks,block_to_block_type, BlockType
from textnode import TextType, TextNode
from split_delimeter import text_to_textnodes, split_nodes_delimiter, split_nodes_image, split_nodes_link
from htmlnode import HTMLNode, text_node_to_html_node, ParentNode, LeafNode

def text_to_children(block):
    new_node = text_to_textnodes(block)
    new_list = []
    for node in new_node:
        new_list.append(text_node_to_html_node(node))
    return new_list

def normalize(text):
    return " ".join(text.strip().split())

def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    all_children = []
    for block in blocks:
        html_node = None
        block_type = block_to_block_type(block)

        if block_type == BlockType.PARAGRAPH:
            block = normalize(block)
            children = text_to_children(block)
            if not children:
                continue
            html_node = ParentNode('p',  children)

        if block_type == BlockType.HEADING:
            if block.startswith('# '): 
                block = normalize(block[2:])
                children = text_to_children(block)
                if not children:
                    continue
                html_node = ParentNode('h1',children)
            elif  block.startswith('## '):
                block = normalize(block[3:])
                children = text_to_children(block)
                if not children:
                    continue
                html_node = ParentNode('h2',children)
            elif  block.startswith('### ') :
                block = normalize(block[4:])
                children = text_to_children(block)
                if not children:
                    continue
                html_node = ParentNode('h3',children)
            elif block.startswith('#### '):
                block = normalize(block[5:])
                children = text_to_children(block)
                if not children:
                    continue
                html_node = ParentNode('h4',children)
            elif   block.startswith('##### '):
                block = normalize(block[6:])
                children = text_to_children(block)
                if not children:
                    continue
                html_node = ParentNode('h5',children)
            elif   block.startswith('###### '):
                block = normalize(block[7:])
                children = text_to_children(block)
                if not children:
                    continue
                html_node = ParentNode('h6',children)

        if block_type == BlockType.CODE:
            child = block.split('\n') 
            if child and child[0].strip().startswith('```'):
                child = child[1:]
            if child and child[-1].strip().startswith('```'):
                child = child[:-1]
            import textwrap
            code_text = textwrap.dedent('\n'.join(child))
            if not code_text.endswith('\n'):
               code_text += '\n'
            children_html = LeafNode('code',code_text)
            html_node = ParentNode('pre',[children_html])

        if block_type == BlockType.UNORDERED_LIST:
            list_items = []
            inner = block.split('\n')
            for line in inner:
                item_text = normalize(line[2:])
                children = text_to_children(item_text)
                if not children:
                    continue
                list_items.append(ParentNode('li',  children))
            if not list_items:
                continue
            html_node = ParentNode('ul',list_items)

        if block_type == BlockType.ORDERED_LIST:
            list_items = []
            inner = block.split('\n')
            for line in inner:
                item_text = normalize(line[3:]) 
                children = text_to_children(item_text)
                if not children:
                    continue
                list_items.append(ParentNode('li',  children))
            if not list_items:
                continue
            html_node = ParentNode('ol',list_items)

        if block_type == BlockType.QUOTE:
            lines= block.split('\n')
            new_lines = []
            for line in lines:
                if not line.startswith('>'):
                    raise ValueError("invalid quote block")
                new_lines.append(line[2:].strip())
            block = ' '.join(new_lines)
            children = text_to_children(block)
            if not children:
                continue
            html_node = ParentNode('blockquote',children)

        if html_node is not None:
            all_children.append(html_node)
        else:
            print("Skipped block:", repr(block), "type:", block_type)

    main_html_node = ParentNode('div',all_children)
    return main_html_node

def extract_title(markdown):
    blocks = markdown_to_blocks(markdown)
    for block in blocks:
        block_type = block_to_block_type(block)
        if block_type == BlockType.HEADING:
            if block.startswith('# '): 
                john = normalize(block[2:])
    return john
