import os
import re
import urllib.request
import ssl
from urllib.parse import urlparse

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"
images_dir = os.path.join(base_dir, "images", "uploads")

if not os.path.exists(images_dir):
    os.makedirs(images_dir)

# Regex to find http/https URLs that look like images
pattern = re.compile(r'https?://[^\s"\'\)]+\.(?:png|jpg|jpeg|webp|gif|svg)(?:\?[^\s"\'\)]*)?', re.IGNORECASE)

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

def get_clean_filename(url):
    parsed = urlparse(url)
    filename = os.path.basename(parsed.path)
    if not filename:
        filename = "image_" + str(hash(url)) + ".jpg"
    return filename

def download_image(url):
    filename = get_clean_filename(url)
    local_path = os.path.join(images_dir, filename)
    if not os.path.exists(local_path):
        print(f"Downloading {url} to {local_path}...")
        try:
            req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
            with urllib.request.urlopen(req, context=ctx) as response, open(local_path, 'wb') as out_file:
                out_file.write(response.read())
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return None
    else:
        print(f"Already exists: {local_path}")
    return f"images/uploads/{filename}"

for root, _, files in os.walk(base_dir):
    # skip .git or node_modules or images dir if any
    if '.git' in root or 'node_modules' in root or 'images' in root:
        continue
    for file in files:
        if file.endswith(('.html', '.css', '.js')):
            full_path = os.path.join(root, file)
            with open(full_path, 'r', encoding='utf-8') as f:
                content = f.read()
            
            matches = pattern.findall(content)
            if matches:
                print(f"Processing {full_path} - found {len(matches)} potential image links.")
                updated = False
                for url in set(matches):
                    # We might have local host links or similar, but regex ensures it has http:// or https://
                    local_rel_path = download_image(url)
                    if local_rel_path:
                        content = content.replace(url, local_rel_path)
                        updated = True
                
                if updated:
                    with open(full_path, 'w', encoding='utf-8') as f:
                        f.write(content)
                    print(f"Updated {full_path}")

print("Done.")
