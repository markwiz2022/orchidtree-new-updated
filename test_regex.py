import urllib.request
import re

url = 'https://drive.google.com/drive/folders/1mmn2kBzAzSUo3GMIFNxo68r4pYQNqhbp'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    matches = re.findall(r'\[\"([a-zA-Z0-9_-]{33})\",\"([^\"]+\.(?:JPG|jpg))\"', html)
    print('Pattern 1 matches:', len(matches))
    for m in matches:
        print(m)
        
    if not matches:
        matches2 = re.findall(r'\"([a-zA-Z0-9_-]{33})\"[^\"]*?\"([^\"]+\.(?:JPG|jpg))\"', html)
        print('Pattern 2 matches:', len(matches2))
        for m in matches2:
            print(m)
except Exception as e:
    print(e)
