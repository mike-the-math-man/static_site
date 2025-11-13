from enum import Enum

def markdown_to_blocks(markdown):
    split = markdown.split('\n\n')
    final = []
    for s in split:
        if s !="":
            final.append(s.strip())
    return final

class BlockType(Enum):
    PARAGRAPH = 'paragraph'
    HEADING = 'heading'
    CODE = 'code'
    QUOTE = 'quote'
    UNORDERED_LIST = 'unordered_list'
    ORDERED_LIST = 'ordered_list'

def block_to_block_type(markdown_block):
    if markdown_block.startswith('# ') or markdown_block.startswith('## ') or markdown_block.startswith('### ') or markdown_block.startswith('#### ') or markdown_block.startswith('##### ') or markdown_block.startswith('###### '):
            return BlockType.HEADING
    elif markdown_block.startswith('```') and markdown_block.endswith('```'):
         return BlockType.CODE
    elif markdown_block.startswith('>'):
        return BlockType.QUOTE
    elif markdown_block.startswith('- '):
        return BlockType.UNORDERED_LIST
    elif markdown_block.startswith('1. '):
        all_lines = markdown_block.split('\n')
        for i in range(len(all_lines)):
            if not all_lines[i].startswith(f'{i+1}. '):
                return BlockType.PARAGRAPH
        return BlockType.ORDERED_LIST
    else:
        return BlockType.PARAGRAPH



