import re
import requests
from bs4 import BeautifulSoup
res = requests.get('https://orchidtree.in/experiences')
soup = BeautifulSoup(res.text, 'html.parser')
for div in soup.find_all(style=True):
    style = div['style']
    match = re.search(r'background-image:\s*url\([\'"]?(.*?)[\'"]?\)', style)
    if match:
        parent = div.get_text(strip=True)[:50]
        print(match.group(1), '||', parent)
