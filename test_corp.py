import urllib.request
import re

url = 'https://drive.google.com/drive/folders/1jyElHR3QACU4YkRun-lRsOOZfwBsWKZS'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    # Find any file name pattern
    matches = re.findall(r'([a-zA-Z0-9_\-\s]+\.(?:JPG|jpg|jpeg|png|mp4|MP4|HEIC|heic))[^<]*?([a-zA-Z0-9_-]{33})', html)
    print("Files found:", matches[:5])
except Exception as e:
    print(e)
