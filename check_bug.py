import os

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

start = content.find('mgStart')
start2 = content.find('background-image:url', start)
print(content[start2-50:start2+150])
