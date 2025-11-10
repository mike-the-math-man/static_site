from textnode import TextNode, TextType
from extract_markdown_images import extract_markdown_images, extract_markdown_links

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_list = []
    for old in old_nodes:
        if old.TextType != TextType.TEXT:
            new_list.append(old)
            continue

        split_list = old.text.split(delimiter)
        if len(split_list)%2 ==0:
            raise Exception("that's invalid Markdown syntax")
        for i in range(0,len(split_list)-1,2):
            if split_list[i] != "":
                new_list.append(TextNode(split_list[i],TextType.TEXT))
            new_list.append(TextNode(split_list[i+1],text_type))
        if split_list[-1] !="":
            new_list.append(TextNode(split_list[-1],TextType.TEXT))
    return new_list
        
def split_nodes_image(old_nodes):
    new_list = []
    for old in old_nodes:
        if old.TextType != TextType.TEXT:
            new_list.append(old)
            continue

        image_tuples = extract_markdown_images(old.text)
        appendable = old.text
        if len(image_tuples) == 0:
            new_list.append(old)
            continue
        for tuple in image_tuples:
            split_list = appendable.split(f"![{tuple[0]}]({tuple[1]})")
            if len(split_list)!=2:
                raise ValueError("Invalid markdown")
            if split_list[0] != "":
                new_list.append(TextNode(split_list[0],TextType.TEXT))
            new_list.append(TextNode(tuple[0],TextType.IMAGE,tuple[1]))

            appendable = split_list[1]
        if appendable != "":
            new_list.append(TextNode(appendable,TextType.TEXT))
    return new_list

def split_nodes_link(old_nodes):
    new_list = []
    for old in old_nodes:
        if old.TextType != TextType.TEXT:
            new_list.append(old)
            continue

        link_tuples = extract_markdown_links(old.text)
        appendable = old.text
        if len(link_tuples) == 0:
            new_list.append(old)
            continue
        for tuple in link_tuples:
            split_list = appendable.split(f"[{tuple[0]}]({tuple[1]})")
            if len(split_list)!=2:
                raise ValueError("Invalid markdown")
            if split_list[0] != "":
                new_list.append(TextNode(split_list[0],TextType.TEXT))
            new_list.append(TextNode(tuple[0],TextType.LINK,tuple[1]))

            appendable = split_list[1]
        if appendable != "":
            new_list.append(TextNode(appendable,TextType.TEXT))
    return new_list

