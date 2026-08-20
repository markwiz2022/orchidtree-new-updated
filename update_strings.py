import os

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\shared\catalog.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("American Standard Queen Size Bed", "American Std Queen Size Bed")
content = content.replace("King Bed + Queen Size Pull-Out Bed", "King + Queen Size Pull-Out Bed")
content = content.replace("Contemporary Bedding", "Contemporary Bathing")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated catalog.js strings")
