from markdown_to_html_node import markdown_to_html_node, extract_title
import os
import shutil



def generate_page(from_path, template_path, dest_path):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path, "r",encoding="utf-8") as file_object:
        markdown = file_object.read()
    #markdown = open(from_path, "r")
    with open(template_path, "r",encoding="utf-8") as file_object:
        template = file_object.read()
    #template = open(template_path, "r")
    content = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace('{{ Title }}',title)
    template  = template.replace('{{ Content }}',content)
    dirpath = os.path.dirname(dest_path)
    if dirpath:
        os.makedirs(dirpath, exist_ok=True)
    with open(dest_path, "w", encoding="utf-8") as f:
        f.write(template)

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)

    with open(template_path, "r",encoding="utf-8") as file_object:
        template = file_object.read()

    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_file = filename
        if '.' in filename:
            dest_file = filename.split('.')[0] + '.html'
        dest_path = os.path.join(dest_dir_path, dest_file)
        print(f"Generating page from {from_path} to {dest_path} using {template_path}")
        if os.path.isfile(from_path):
            with open(from_path, "r",encoding="utf-8") as file_object:
                markdown = file_object.read()
            content = markdown_to_html_node(markdown).to_html()
            title = extract_title(markdown)
            template = template.replace('{{ Title }}',title)
            template  = template.replace('{{ Content }}',content)
            dirpath = os.path.dirname(dest_path)
            if dirpath:
                os.makedirs(dirpath, exist_ok=True)
            with open(dest_path, "w", encoding="utf-8") as f:
                f.write(template)
        else:
            generate_pages_recursive(from_path, template_path, dest_path)

