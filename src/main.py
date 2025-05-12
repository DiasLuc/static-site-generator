from textnode import TextNode, TextType
import os, shutil
from markdownblocks import markdown_to_html_node
from pathlib import Path
import sys
def main():
    if len(sys.argv) == 1:
        basepath = '/'
    else:
        basepath = sys.argv[1]

    new_text_node = TextNode('This is a text node', TextType.BOLD,'https://www.boot.dev')
    static_dir = './static/'
    public_dir = './docs/'
    clear_dir(public_dir)
    copy_content(static_dir, public_dir)
    extract_title('src/content/index.md')

    content_loc = 'src/content/'
    template_loc = 'template.html'
    dest_loc = 'docs/'
    
    generate_pages_recursive(content_loc, template_loc, dest_loc, basepath)



# C5 L1
def clear_dir(dir):
    dir_list = os.listdir(dir)
    if dir_list != []:
        shutil.rmtree(dir)
        os.mkdir(dir)
def copy_content(source_dir, destination_dir):
    source_dir_list = os.listdir(source_dir)
    for item in source_dir_list:
        item_path = os.path.join(source_dir, item)
        # print(f"item path is: {item_path}")
        if os.path.isfile(item_path):
            new_dest_dir = os.path.join(destination_dir, item)
            shutil.copy(item_path, new_dest_dir)
        if os.path.isdir(item_path):
            new_dest = os.path.join(destination_dir,item)
            os.makedirs(new_dest, exist_ok=True)
            new_source = os.path.join(source_dir,item)
            copy_content(new_source, new_dest)
    
    
# C5 L2
def extract_title(markdown):
    with open(markdown, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
        raise Exception("There is no h1 header")
            
def generate_page(from_path, template_path, dest_path, basepath):
    # print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    from_file = open(from_path, 'r', encoding="utf-8")
    markdown = from_file.read()
    from_file.close()
    
    template_file = open(template_path, 'r', encoding="utf-8")
    template = template_file.read()
    template_file.close()

    markdown_node = markdown_to_html_node(markdown)
    markdown_as_html = ""
    
    for node in markdown_node.children:
        markdown_as_html += node.to_html()
    
    title = extract_title(from_path)
    updated_template = template.replace('{{ Title }}', title)
    updated_template = updated_template.replace('{{ Content }}', markdown_as_html)

    #C5 L5
    updated_template = updated_template.replace('href="/', f'href="{basepath}')
    updated_template = updated_template.replace('src="/', f'src="{basepath}')
    
    dest_dir_path = os.path.dirname(dest_path)
    if dest_dir_path != "":
        os.makedirs(dest_dir_path, exist_ok=True)
    index_f = open(dest_path, 'w', encoding="utf-8")
    index_f.write(updated_template)
    
    index_f.close()
# C5 L3
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    
    content_dir_list = os.listdir(dir_path_content)
    for item in content_dir_list:
        # Skip hidden system files like .DS_Store
        if item.startswith('.'):
            continue
        item_path = os.path.join(dir_path_content, item)
        # print(f"item path is: {item_path}")
        name, ext = os.path.splitext(item)
        if os.path.isfile(item_path):
            item = name + ".html"
            destination_path = os.path.join(dest_dir_path, item)            


            output_dir = os.path.dirname(destination_path)
            os.makedirs(output_dir, exist_ok=True)
            print(f"Processing: {item_path} -> {destination_path}")
            try:
                generate_page(item_path, template_path, destination_path, basepath)
            except UnicodeDecodeError as e:
                print(f"DECODE ERROR in file: {item_path}")
                print(f"Error details: {e}")
                # Optionally continue instead of stopping
                continue
        elif os.path.isdir(item_path):
            new_dest = os.path.join(dest_dir_path,item)
            os.makedirs(new_dest, exist_ok=True)
            new_source = os.path.join(dir_path_content,item)
            generate_pages_recursive(new_source, template_path, new_dest, basepath)
main()