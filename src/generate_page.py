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
    if not os.path.exists(os.path.dirname(dest_path)):
        os.mkdir(os.path.dirname(dest_path))
    with open(dest_path, "w") as f:
        f.write(template)
 