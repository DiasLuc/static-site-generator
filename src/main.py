from textnode import TextNode, TextType
import os, shutil
from markdownblocks import markdown_to_html_node
def main():
    new_text_node = TextNode('This is a text node', TextType.BOLD,'https://www.boot.dev')
    static_dir = './static/'
    public_dir = './public/'
    copy_content(static_dir, public_dir)
    extract_title('src/content/index.md')

    markdown_loc = 'src/content/index.md'
    template_loc = 'template.html'
    dest_loc = 'public/index.html'
    generate_page(markdown_loc, template_loc, dest_loc)



# C5 L1
def clear_dir(dir):
    dir_list = os.listdir(dir)
    if dir_list != []:
        shutil.rmtree(dir)
        os.mkdir(dir)
def copy_content(source_dir, destination_dir):
    clear_dir(destination_dir)
    source_dir_list = os.listdir(source_dir)
    for item in source_dir_list:
        item_path = os.path.join(source_dir, item)
        # print(f"item path is: {item_path}")
        if os.path.isfile(item_path):
            new_dest_dir = os.path.join(destination_dir, item)
            shutil.copy(item_path, new_dest_dir)
        if os.path.isdir(item_path):
            new_dest = os.path.join(destination_dir,item)
            os.mkdir(new_dest)
            new_source = os.path.join(source_dir,item)
            copy_content(new_source, new_dest)
    
    
# C5 L2
def extract_title(markdown):
    with open(markdown, encoding="utf-8") as f:
        for line in f:
            if line.startswith("# "):
                return line[2:].strip()
        raise Exception("There is no h1 header")
            
def generate_page(from_path, template_path, dest_path):
    # print(f'Generating page from {from_path} to {dest_path} using {template_path}')
    markdown_f = open(from_path, 'r', encoding="utf-8")
    template_f = open(template_path, 'r', encoding="utf-8")
    markdown = markdown_f.read()
    template = template_f.read()
    markdown_node = markdown_to_html_node(markdown)
    markdown_as_html = ""
    template_f.close()
    for node in markdown_node.children:
        markdown_as_html += node.to_html()
    
    title = extract_title(from_path)
    updated_template = template.replace(' {{ Title }} ', title)
    updated_template = updated_template.replace('{{ Content }}', markdown_as_html)
    index_f = open(dest_path, 'x', encoding='utf-8')
    index_f.write(updated_template)
    markdown_f.close()
    template_f.close()
    index_f.close()

main()