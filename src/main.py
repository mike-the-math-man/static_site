from textnode import TextNode, TextType
import os
import shutil
from generate_page import generate_page



def delete_and_copy(destination_path,start_path):
    destination_path = os.path.expanduser(destination_path)
    start_path = os.path.expanduser(start_path)
    if os.path.exists(destination_path) and not os.path.isfile(destination_path):
        shutil.rmtree(destination_path, ignore_errors=False, onexc=None, dir_fd=None)
    if not os.path.exists(destination_path) and not os.path.isfile(destination_path):
        os.mkdir(destination_path)
    if not os.path.exists(start_path):
        return
    if not os.path.isfile(start_path):
        paths = os.listdir(start_path)
        for path in paths:
            src_child = os.path.join(start_path, path)
            dst_child  = os.path.join(destination_path, path)
            if os.path.isfile(src_child):
                shutil.copy(src_child, dst_child)
            else:
                if not os.path.exists(dst_child):
                    os.mkdir(dst_child)
                delete_and_copy(dst_child,src_child)


          
def main():
    shutil.rmtree( os.path.expanduser("~/static_site/public"), ignore_errors=False, onexc=None, dir_fd=None)
    delete_and_copy("~/static_site/public", "~/static_site/static")
    generate_page("content/index.md", "template.html", "public/index.html")


main()