import re
import os

urls = [
    'https://images.unsplash.com/photo-1583939000148-774d08439df2?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1595964270729-c8e580d38101?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1621865397491-039c97b8ea0e?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1550692797-2a4501aeb42e?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1610173826622-485c96078db0?auto=format&fit=crop&w=1200&q=80',
    'https://images.unsplash.com/photo-1600093463592-8e36ae95ef56?auto=format&fit=crop&w=1200&q=80'
]

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\weddings.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    
content = re.sub(r'(<img class="hero-img" src=")[^"]+(")', r'\g<1>' + urls[0] + r'\g<2>', content)

uploads = re.findall(r'src="(images/uploads/[^"]+)"', content)
uploads = list(set(uploads)) 

for i, up in enumerate(uploads):
    if i+1 < len(urls):
        content = content.replace(up, urls[i+1])
        
with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
    
print("Updated weddings.html with Unsplash Indian wedding images!")
