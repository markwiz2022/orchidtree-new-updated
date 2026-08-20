import os
filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    idx = content.find('mGallery')
    print(content[max(0, idx-100):idx+500])
