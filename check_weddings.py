import os
import re

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\weddings.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    
print(re.findall(r'<img [^>]*src="([^"]+)"', content))
