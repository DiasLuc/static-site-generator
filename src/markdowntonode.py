from textnode import TextType, TextNode, Enum
import re

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

def extract_markdown_images(text):
    matches = re.findall(r"\!\[(.*?)\]\((.*?)\)",text)
    return matches

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)",text)
    return matches

def split_nodes_image(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if extract_markdown_images(node.text) == []:
            new_nodes.append(node)
            continue #skip to next node!!
        
        remaining_text = node.text
        images = extract_markdown_images(node.text)

        for image in images:
            alt_text, image_link = image

            sections = remaining_text.split(f"![{alt_text}]({image_link})", 1)
            if sections[0]: 
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(alt_text, TextType.IMAGE, image_link))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))    
    return new_nodes


def split_nodes_link(old_nodes):
    new_nodes = []
    for node in old_nodes:
        if extract_markdown_links(node.text) == []:
            new_nodes.append(node)
            continue #skip to next node!!
        
        remaining_text = node.text
        links = extract_markdown_links(node.text)

        for link in links:
            link_text, link_url = link

            sections = remaining_text.split(f"[{link_text}]({link_url})", 1)
            if sections[0]: 
                new_nodes.append(TextNode(sections[0],TextType.TEXT))
            new_nodes.append(TextNode(link_text, TextType.LINK, link_url))
            remaining_text = sections[1]
        if remaining_text:
            new_nodes.append(TextNode(remaining_text, TextType.TEXT))    
    return new_nodes