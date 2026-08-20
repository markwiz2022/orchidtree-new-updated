import urllib.request
import re

url = 'https://drive.google.com/drive/folders/1GoApXpJLjTKFY4yIZ8OpS_45sbYGOIDD'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Try finding subfolder names and IDs
    # Usually they look like ["Name", "ID"] where ID is 33 chars.
    matches = re.findall(r'\["([^"]+)",\s*"([a-zA-Z0-9_-]{33})"', html)
    print("Potential Folders:")
    for m in matches:
        if m[0] not in ('application/vnd.google-apps.folder', 'Image'):
            print(f"- {m[0]} : {m[1]}")
except Exception as e:
    print(e)
