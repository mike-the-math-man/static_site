import unittest
from markdown_to_blocks import markdown_to_blocks,block_to_block_type, BlockType


class TestTextToNode(unittest.TestCase):
    
    def test_markdown_to_blocks(self):
        md = """
This is **bolded** paragraph

This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

    def test_markdown_to_blocks_newlines(self):
        md = """
This is **bolded** paragraph




This is another paragraph with _italic_ text and `code` here
This is the same paragraph on a new line

- This is a list
- with items
"""
        blocks = markdown_to_blocks(md)
        self.assertEqual(
            blocks,
            [
                "This is **bolded** paragraph",
                "This is another paragraph with _italic_ text and `code` here\nThis is the same paragraph on a new line",
                "- This is a list\n- with items",
            ],
        )

class test_block_type(unittest.TestCase):
    def test_heading1(self):
        block = '# Heading 1'
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_heading2(self):
        block = '## Heading 2'
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_heading3(self):
        block = '### Heading 3'
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_heading4(self):
        block = '#### Heading 4'
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_heading5(self):
        block = '##### Heading 5'
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_heading6(self):
        block = '###### Heading 6'
        self.assertEqual(block_to_block_type(block),BlockType.HEADING)

    def test_heading7(self):
        block = '####### Heading 6'
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

    def test_paragraph(self):
        block = 'This is a paragraph of text.'
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)

    def test_unordered_list(self):
        block = '- Item 1\n- Item 2\n- Item 3'
        self.assertEqual(block_to_block_type(block),BlockType.UNORDERED_LIST)

    def test_ordered_list(self):
        block = '1. Item 1\n2. Item 2\n3. Item 3'
        self.assertEqual(block_to_block_type(block),BlockType.ORDERED_LIST)

    def test_code(self):
        block = '```\nThis is code\n```'
        self.assertEqual(block_to_block_type(block),BlockType.CODE)

    def test_code(self):
        block = '> This is a quote.'
        self.assertEqual(block_to_block_type(block),BlockType.QUOTE)

    def test_wrongly_ordered_list(self):
        block = '1. Item 1\n3. Item 2\n2. Item 3'
        self.assertEqual(block_to_block_type(block),BlockType.PARAGRAPH)
    
    def test_block_to_block_types(self):
        block = "# heading"
        self.assertEqual(block_to_block_type(block), BlockType.HEADING)
        block = "```\ncode\n```"
        self.assertEqual(block_to_block_type(block), BlockType.CODE)
        block = "> quote\n> more quote"
        self.assertEqual(block_to_block_type(block), BlockType.QUOTE)
        block = "- list\n- items"
        self.assertEqual(block_to_block_type(block), BlockType.UNORDERED_LIST)
        block = "1. list\n2. items"
        self.assertEqual(block_to_block_type(block), BlockType.ORDERED_LIST)
        block = "paragraph"
        self.assertEqual(block_to_block_type(block), BlockType.PARAGRAPH)

if __name__ == "__main__":
    unittest.main()