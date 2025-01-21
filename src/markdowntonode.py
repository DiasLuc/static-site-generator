from textnode import TextType, TextNode, Enum


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            new_nodes.append(node)
            continue #skip to next node!!
        current_index = 0
        remaining_text = node.text

        while delimiter in remaining_text:
            first_delimiter_index = remaining_text.find(delimiter)
            if first_delimiter_index == -1:
                break
            
            if first_delimiter_index > 0:
                new_nodes.append(TextNode(remaining_text[0:first_delimiter_index], TextType.TEXT))

            second_delimiter_index = remaining_text.find(delimiter, first_delimiter_index + 1)
            if second_delimiter_index == -1:
                raise Exception("Missing Closing Delimiter")
            
            new_nodes.append(TextNode(remaining_text[first_delimiter_index+1:second_delimiter_index], text_type))
                
            remaining_text = remaining_text[second_delimiter_index +1:]

        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))
    return new_nodes

# node = TextNode("Here is `code` and more `code`", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)

# print(f"New Nodes = {new_nodes}")
