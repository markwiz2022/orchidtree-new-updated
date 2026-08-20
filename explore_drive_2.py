import urllib.request
import re

url = 'https://drive.google.com/drive/folders/1GoApXpJLjTKFY4yIZ8OpS_45sbYGOIDD'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find all 33-char IDs and just a bit of context around them
    matches = re.findall(r'.{0,30}([a-zA-Z0-9_-]{33}).{0,30}', html)
    print(f"Found {len(matches)} IDs.")
    # But this might be too noisy. Let's look for "aria-label" which is used for files/folders.
    matches = re.findall(r'aria-label="([^"]+)"[^>]*?([a-zA-Z0-9_-]{33})', html)
    print("Aria label matches:")
    for m in matches:
        print(f"- {m[0]} : {m[1]}")
except Exception as e:
    print(e)
