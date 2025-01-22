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
            return f"heading {heading_number}"
    
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
    