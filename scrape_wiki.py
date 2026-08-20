import urllib.request
import re
import os
import ssl
import json

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "https://en.wikipedia.org/w/api.php?action=query&format=json&prop=imageinfo&iiprop=url&generator=categorymembers&gcmtitle=Category:Hindu_weddings_in_India&gcmtype=file&gcmlimit=20"
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    data = json.loads(html)
    pages = data['query']['pages']
    urls = []
    for k, v in pages.items():
        if 'imageinfo' in v:
            urls.append(v['imageinfo'][0]['url'])
    print(urls)
except Exception as e:
    print(e)
