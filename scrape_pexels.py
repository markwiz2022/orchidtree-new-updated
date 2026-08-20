import urllib.request
import re
import os
import ssl

ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

req = urllib.request.Request('https://www.pexels.com/search/indian%20wedding/', headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
try:
    html = urllib.request.urlopen(req, context=ctx).read().decode('utf-8')
    images = re.findall(r'https://images\.pexels\.com/photos/\d+/pexels-photo-\d+\.jpeg', html)
    images = list(set(images))
    print(images[:10])
except Exception as e:
    print(e)
