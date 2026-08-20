import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"
upload_dir = os.path.join(base_dir, "images", "uploads")
os.makedirs(upload_dir, exist_ok=True)

urls_to_scrape = [
    "https://orchidtree.in/",
    "https://orchidtree.in/stays",
    "https://orchidtree.in/experiences",
    "https://orchidtree.in/weddings",
    "https://orchidtree.in/corporate",
    "https://orchidtree.in/about"
]

downloaded = set()
image_contexts = []

for url in urls_to_scrape:
    print(f"Scraping {url}...")
    try:
        res = requests.get(url, timeout=10)
        soup = BeautifulSoup(res.text, 'html.parser')
        
        # Find all images
        for img in soup.find_all('img'):
            src = img.get('src')
            if not src: continue
            full_url = urljoin(url, src)
            if not full_url.startswith('http'): continue
            alt = img.get('alt', '')
            
            # Find surrounding text (parent or previous sibling)
            parent_text = img.parent.get_text(strip=True)[:50] if img.parent else ""
            
            image_contexts.append({'url': full_url, 'alt': alt, 'context': parent_text, 'page': url})
            
        # Find inline backgrounds
        for div in soup.find_all(style=True):
            style = div['style']
            match = re.search(r'background-image:\s*url\([\'"]?(.*?)[\'"]?\)', style)
            if match:
                src = match.group(1)
                full_url = urljoin(url, src)
                if not full_url.startswith('http'): continue
                
                parent_text = div.get_text(strip=True)[:50]
                image_contexts.append({'url': full_url, 'alt': 'background', 'context': parent_text, 'page': url})
                
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")

# Download and map
url_to_local = {}

print(f"Found {len(image_contexts)} image references.")
for item in image_contexts:
    url = item['url']
    if url in downloaded:
        continue
        
    filename = url.split('/')[-1]
    if '?' in filename:
        filename = filename.split('?')[0]
        
    local_path = os.path.join(upload_dir, filename)
    
    if not os.path.exists(local_path):
        try:
            r = requests.get(url, timeout=10)
            if r.status_code == 200:
                with open(local_path, 'wb') as f:
                    f.write(r.content)
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            continue
            
    downloaded.add(url)
    url_to_local[url] = filename
    item['local'] = filename

# Output context report
with open(os.path.join(base_dir, "image_report.txt"), "w", encoding="utf-8") as f:
    for item in image_contexts:
        if 'local' in item:
            f.write(f"Local: {item['local']}\nPage: {item['page']}\nAlt: {item['alt']}\nContext: {item['context']}\nURL: {item['url']}\n---\n")

print("Done downloading and mapping.")
