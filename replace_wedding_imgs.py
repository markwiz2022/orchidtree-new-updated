import urllib.request
import json
import re
import os

req = urllib.request.Request('https://unsplash.com/napi/search/photos?query=indian+wedding&per_page=10', headers={'User-Agent': 'Mozilla/5.0'})
try:
    resp = urllib.request.urlopen(req).read()
    data = json.loads(resp)
    urls = [res['urls']['regular'] for res in data['results']]
    
    filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\weddings.html'
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    # Find existing gallery images and replace them
    # <div class="fmedia"><img src="..."
    # There's also the hero image: class="hero-img" src="..."
    
    # We will replace the 3 images in the gallery grid and maybe the hero.
    # The gallery grid in weddings.html:
    # "images/uploads/Image6_scaled_jpg_083e47ab4a.webp"
    # "images/uploads/Copy_of_2_a5beee287f.jpg"
    # ... wait, let's just use regex to replace all <img src="..."> that look like they are in the weddings page, except the logo.
    
    # Let's replace the hero:
    content = re.sub(r'(<img class="hero-img" src=")[^"]+(")', r'\g<1>' + urls[0] + r'\g<2>', content)
    
    # The gallery images:
    # Let's just find all img tags with src="images/uploads/..."
    uploads = re.findall(r'src="(images/uploads/[^"]+)"', content)
    uploads = list(set(uploads)) # unique
    
    for i, up in enumerate(uploads):
        if i+1 < len(urls):
            content = content.replace(up, urls[i+1])
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
    print("Replaced wedding images with:", urls[:len(uploads)+1])
except Exception as e:
    print(e)
