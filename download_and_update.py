import os
import re
import urllib.request
from urllib.parse import urljoin

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"
uploads_url = "https://orchidtree.in/uploads/"
images_dir = os.path.join(base_dir, "images", "uploads")

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

files_to_process = [
    "index.html",
    "experiences.html",
    os.path.join("shared", "catalog.js")
]

# Regex to find 'images/uploads/filename' or "images/uploads/filename"
pattern = re.compile(r'[\'"]images/uploads/([^\'"]+)[\'"]')

import ssl

def download_image(filename):
    url = urljoin(uploads_url, filename)
    local_path = os.path.join(images_dir, filename)
    if not os.path.exists(local_path):
        print(f"Downloading {url} to {local_path}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            ctx = ssl.create_default_context()
            ctx.check_hostname = False
            ctx.verify_mode = ssl.CERT_NONE
            with urllib.request.urlopen(req, context=ctx) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {filename}: {e}")
    else:
        print(f"Already exists: {local_path}")
    return f"images/uploads/{filename}"

for filepath in files_to_process:
    full_path = os.path.join(base_dir, filepath)
    if not os.path.exists(full_path):
        print(f"File not found: {full_path}")
        continue
        
    print(f"Processing {full_path}...")
    with open(full_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    matches = pattern.findall(content)
    if matches:
        for filename in set(matches):
            local_rel_path = download_image(filename)
            # Replace U+'filename' with 'images/uploads/filename'
            content = content.replace(f"U+'{filename}'", f"'{local_rel_path}'")
            # Replace U+"filename" with "images/uploads/filename"
            content = content.replace(f'U+"{filename}"', f'"{local_rel_path}"')
        
        with open(full_path, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {full_path}")
    else:
        print(f"No matches found in {full_path}")

print("Done.")
