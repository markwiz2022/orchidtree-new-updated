import requests
from bs4 import BeautifulSoup
import re
import urllib.parse

def get_live_images(url):
    print(f"Checking {url}")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, 'html.parser')
    
    images = set()
    # Find all img tags
    for img in soup.find_all('img'):
        src = img.get('src')
        if src:
            images.add(src)
            
    # Find all inline styles with background-image
    for tag in soup.find_all(style=True):
        style = tag['style']
        match = re.search(r'background(?:-image)?:\s*url\([\'"]?(.*?)[\'"]?\)', style)
        if match:
            images.add(match.group(1))
            
    # Also just regex search the whole raw HTML for anything ending in image extensions
    raw_matches = re.findall(r'[\'"](/[^\'"]+\.(?:jpg|jpeg|png|webp|svg))[\'"]', res.text)
    for rm in raw_matches:
        images.add(rm)
        
    for img in sorted(images):
        print("  ->", img)

get_live_images('https://orchidtree.in/')
get_live_images('https://orchidtree.in/experiences')
get_live_images('https://orchidtree.in/gallery') # just in case
get_live_images('https://orchidtree.in/about')
