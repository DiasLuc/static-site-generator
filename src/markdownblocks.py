def markdown_to_blocks(markdown):
    blocks =  markdown.split(f"\n\n")
    modified_blocks = []
    for block in blocks:
       modded_block = block.strip()
       if modded_block != "":
           modified_blocks.append(modded_block)
    return modified_blocks
