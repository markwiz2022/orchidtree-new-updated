import urllib.request
import re
import os

req = urllib.request.Request('https://unsplash.com/s/photos/indian-wedding', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    images = re.findall(r'https://images\.unsplash\.com/photo-[a-zA-Z0-9-]+[^\"]+', html)
    # filter out profile pics
    bases = list(set([img for img in images if 'w=1000' in img or 'w=800' in img or 'w=1200' in img or 'ixlib=rb' in img]))
    # Just take unique base URLs
    urls = list(set([img.split('?')[0] + '?auto=format&fit=crop&w=1200&q=80' for img in images if 'photo-' in img]))
    
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
        
    print("Replaced wedding images with:", urls[:len(uploads)+1])
except Exception as e:
    print(e)
