from textnode import TextNode, TextType

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
        
