from htmlnode import ParentNode, text_node_to_html_node
from markdowntonode import text_to_textnodes


block_type_paragraph = "paragraph"
block_type_heading = "heading"
block_type_code = "code"
block_type_quote = "quote"
block_type_olist = "ordered_list"
block_type_ulist = "unordered_list"

def markdown_to_blocks(markdown):
    blocks =  markdown.split(f"\n\n")
    modified_blocks = []
    for block in blocks:
       modded_block = block.strip()
       if modded_block != "":
           modified_blocks.append(modded_block)
    return modified_blocks


def block_to_block_type(block):
    if block[0] == "#":
        split = block.split(" ")
        heading_number = split[0].count("#")
        if (heading_number <= 6 
            and heading_number >=1 
            and heading_number == len(split[0])
            and block[heading_number] == " "
        ):
            return "heading"
    
    if len(block) >= 6 and block[0:3] == "```" and block[-3:len(block)] == "```":
        return "code"
    
    lines = block.split("\n")
    if all(line.startswith(">") for line in lines):
        return "quote"
    if all(line.startswith("* ") or line.startswith("- ") for line in lines):
        return "unordered_list"
    
    
    
    if len(lines) < 2:
        return "paragraph"
    if not(lines[0].startswith("1. ")):
            return "paragraph"

    for i, line in enumerate(lines, start=1):
        line_num = i
        parts = line.split(". ")

        
        if not (len(parts) == 2
            and parts[0].isdigit()
            and int(parts[0]) == line_num
        ):
            return "paragraph"
            
    return "ordered_list"
# Ch4 L3
def markdown_to_html_node(markdown):
    blocks = markdown_to_blocks(markdown)
    children = []
    for block in blocks:
        html_node = block_to_html_node(block)
        children.append(html_node)
    return ParentNode("div", children, None)


def block_to_html_node(block):
    block_type = block_to_block_type(block)
    if block_type == block_type_paragraph:
        return paragraph_to_html_node(block)
    if block_type == block_type_heading:
        return heading_to_html_node(block)
    if block_type == block_type_code:
        return code_to_html_node(block)
    if block_type == block_type_olist:
        return olist_to_html_node(block)
    if block_type == block_type_ulist:
        return ulist_to_html_node(block)
    if block_type == block_type_quote:
        return quote_to_html_node(block)
    raise ValueError("Invalid block type")


def text_to_children(text):
    text_nodes = text_to_textnodes(text)
    children = []
    for text_node in text_nodes:
        html_node = text_node_to_html_node(text_node)
        children.append(html_node)
    return children


def paragraph_to_html_node(block):
    lines = block.split("\n")
    paragraph = " ".join(lines)
    children = text_to_children(paragraph)
    return ParentNode("p", children)


def heading_to_html_node(block):
    level = 0
    for char in block:
        if char == "#":
            level += 1
        else:
            break
    if level + 1 >= len(block):
        raise ValueError(f"Invalid heading level: {level}")
    text = block[level + 1 :]
    children = text_to_children(text)
    return ParentNode(f"h{level}", children)


def code_to_html_node(block):
    if not block.startswith("```") or not block.endswith("```"):
        raise ValueError("Invalid code block")
    text = block[4:-3]
    children = text_to_children(text)
    code = ParentNode("code", children)
    return ParentNode("pre", [code])


def olist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[3:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ol", html_items)


def ulist_to_html_node(block):
    items = block.split("\n")
    html_items = []
    for item in items:
        text = item[2:]
        children = text_to_children(text)
        html_items.append(ParentNode("li", children))
    return ParentNode("ul", html_items)


def quote_to_html_node(block):
    lines = block.split("\n")
    new_lines = []
    for line in lines:
        if not line.startswith(">"):
            raise ValueError("Invalid quote block")
        new_lines.append(line.lstrip(">").strip())
    content = " ".join(new_lines)
    children = text_to_children(content)
    return ParentNode("blockquote", children)