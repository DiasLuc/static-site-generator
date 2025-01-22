from textnode import TextNode, TextType
import os, shutil
def main():
    new_text_node = TextNode('This is a text node', TextType.BOLD,'https://www.boot.dev')

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
    static_dir = './static/'
    public_dir = './public/'
    copy_content(static_dir, public_dir)






main()