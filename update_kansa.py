import os

def replace_kansa(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    content = content.replace("{ lbl:'Kayaking',                   img:'images/uploads/kayaking_0K1A7642.JPG' }", 
                              "{ lbl:'Kansa',                      img:'images/uploads/kansa.jpg' }")
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated', filepath)

replace_kansa(r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\index.html')
replace_kansa(r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\experiences.html')
