import os
import re

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"
filepath = os.path.join(base_dir, 'shared', 'menu.js')
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

urls = list(set(re.findall(r'https://images.unsplash.com/[^\s\'"<>]+', content)))
for url in urls:
    content = content.replace(url, 'images/uploads/Copy_of_Barbeque_03_cf30f0f667.jpg')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print(f"Replaced {len(urls)} unsplash placeholders in shared/menu.js")
