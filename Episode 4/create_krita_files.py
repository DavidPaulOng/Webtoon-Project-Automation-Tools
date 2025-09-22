import zipfile
import io
import xml.etree.ElementTree as ET
import shutil
import json 
import ctypes
import os
import re

TEMPLATE_PATH = "../templates"
if not os.path.exists(f"{TEMPLATE_PATH}/template.kra") or not os.path.exists(f"{TEMPLATE_PATH}/options.json"):
    print("❌ Error: Template files aren't found.")
    print("The 'templates' folder needs to be placed inside the project directory")
    input("Press Enter to exit...")
    exit(1)  

# GET TEMPLATE
with open(f"{TEMPLATE_PATH}/template.kra", "rb") as f:
    template = f.read()
template = io.BytesIO(template)

# LOAD OPTIONS
with open(f"{TEMPLATE_PATH}/options.json", "r") as f:
    options = json.load(f)
WIDTH = options["width"]
HEIGHT = options["height"]
SCALE = options["scale"]
PAGES = options["pages"]
CURRENT_SUB_NUM = None
cwd = os.getcwd()
krita_files = [d for d in os.listdir(".") if d.endswith('.kra')]
CURRENT_EPISODE_NUM = int(re.findall(r'\d+$', cwd)[0])
if len(krita_files) > 0:
    CURRENT_SUB_NUM = int(re.findall(r'(\d+)\.kra$', krita_files[-1])[0])


# INPUT NUMBER OF IMAGES OR MODIFY OPTIONS
while True:
    print("--- Create Images ---")
    print(f"Images are of size {WIDTH * SCALE} x ( {HEIGHT * SCALE} x {PAGES} pages ).")
    print("type 'o' to modify options.")
    response = input("Number of Images: ")
    if response.isdigit() and int(response) > 0:
        image_count = int(response)
        break
    elif response.lower() in ['o']:
        while True:
            print("\nInfo: Base Width and Base Height are multiplied by Scale to get the final size of a page.")
            print(f"1. Edit Page Count (current: {PAGES})")
            print(f"2. Edit Scale (current: {SCALE})")
            print(f"3. Edit Base Width (current: {WIDTH})") 
            print(f"4. Edit Base Height (current: {HEIGHT})")
            print(f"5. Back")
            choice = input("\nChoose an option to edit: ")    
            if choice == '1':
                new_page_count = input("Enter new page count (positive integer): ")
                if new_page_count.isdigit() and int(new_page_count) > 0:
                    PAGES = int(new_page_count)
                    options["pages"] = PAGES
                    print("\nPage count updated to {}.\n".format(PAGES))
                    break
                else:
                    print("Invalid input. Page count must be a positive integer.")
            elif choice == '2':
                new_scale = input("Enter new scale (positive integer): ")
                if new_scale.isdigit() and int(new_scale) > 0:
                    SCALE = int(new_scale)
                    options["scale"] = SCALE
                    print("\nScale updated to {}.\n".format(SCALE))
                    break
                else:
                    print("Invalid input. Scale must be a positive integer.")
            elif choice == '3':
                new_width = input("Enter new width (positive integer): ")
                if new_width.isdigit() and int(new_width) > 0:
                    WIDTH = int(new_width)
                    options["width"] = WIDTH
                    print("\nWidth updated to {}.\n".format(WIDTH))
                    break
                else:
                    print("Invalid input. Width must be a positive integer.")
            elif choice == '4':
                new_height = input("Enter new height (positive integer): ")
                if new_height.isdigit() and int(new_height) > 0:
                    HEIGHT = int(new_height)
                    options["height"] = HEIGHT
                    print("\nHeight updated to {}.\n".format(HEIGHT))
                    break
                else:
                    print("Invalid input. Height must be a positive integer.")
            elif choice == '5':
                print("\n")
                break

            with open(f"{TEMPLATE_PATH}/options.json", "w") as f:
                        json.dump(options, f, indent=4)

# # CREATE IMAGES
doctype = b"<!DOCTYPE DOC PUBLIC '-//KDE//DTD krita 2.0//EN' 'http://www.calligra.org/DTD/krita-2.0.dtd'>"
ET.register_namespace('', 'http://www.calligra.org/DTD/krita')
for i in range(image_count):
    copy = io.BytesIO()
    with zipfile.ZipFile(template, mode="r") as src, zipfile.ZipFile(copy, mode="w") as dst:
        for item in src.infolist():
            data = src.read(item.filename)
            if item.filename == "mergedimage.png" or item.filename == "preview.png":
                dst.writestr(item.filename, data, compress_type=zipfile.ZIP_STORED)
            elif item.filename != "maindoc.xml":
                dst.writestr(item, data, compress_type=item.compress_type)
            else:
                with src.open(item) as maindoc:
                    tree = ET.parse(maindoc)
                    root = tree.getroot()
                    root[0].attrib["width"] = str(WIDTH * SCALE)
                    root[0].attrib["height"] = str(HEIGHT * SCALE * PAGES)
                    new_xml_bytes = ET.tostring(root, encoding="UTF-8", xml_declaration=True)
                    # Prepend DOCTYPE manually ( you need to do this because ZipFile compression removes it )
                    new_xml_bytes_with_doctype = new_xml_bytes.replace(b"<?xml version='1.0' encoding='UTF-8'?>", b"<?xml version='1.0' encoding='UTF-8'?>\n" + doctype)
                    dst.writestr(item, new_xml_bytes_with_doctype, compress_type=item.compress_type)
     
        
    copy.seek(0)
    with open(f"Ep {CURRENT_EPISODE_NUM}.{i+1 if not CURRENT_SUB_NUM else CURRENT_SUB_NUM+i+1}.kra", "wb") as out:
        shutil.copyfileobj(copy, out)


# REFRESH EXPLORER
ctypes.windll.shell32.SHChangeNotify(0x8000000, 0x1000, None, None)


