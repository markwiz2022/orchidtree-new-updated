import urllib.request
import re
import gdown
import os

folders = [
    ("cisco", "https://drive.google.com/drive/folders/1jyElHR3QACU4YkRun-lRsOOZfwBsWKZS"),
    ("cisco_output", "https://drive.google.com/drive/folders/1mmn2kBzAzSUo3GMIFNxo68r4pYQNqhbp"),
    ("sagar", "https://drive.google.com/drive/folders/1SBNxGCPB11ZYmKoS6KyseIog2mEXBNPz"),
    ("sap", "https://drive.google.com/drive/folders/1DeptKtp2_XyYeHBquGyxju49FiewIvYf")
]

def download_first_mp4(url, prefix):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        matches = re.findall(r'aria-label=\"([^\"]+\.(?:MP4|mp4))\s+Video.*?ssk=\'\d+:[a-zA-Z0-9]+:([a-zA-Z0-9_-]{33})', html)
        
        if not matches:
            matches = re.findall(r'([^\"]+\.(?:MP4|mp4))[^<]*?([a-zA-Z0-9_-]{33})', html)
            
        if not matches:
            print(f"No MP4 found in {url}")
            return
            
        print(f"Found {len(matches)} MP4 matches for {prefix}.")
        filename, file_id = matches[0]
        
        out_path = f"images/uploads/corp_vid_{prefix}.mp4"
        if not os.path.exists(out_path):
            print(f"Target: {filename} -> ID: {file_id}")
            gdown.download(id=file_id, output=out_path, quiet=True)
            print(f"Downloaded {out_path}")
        else:
            print(f"Already exists: {out_path}")
    except Exception as e:
        print(f"Error on {url}: {e}")

for prefix, url in folders:
    download_first_mp4(url, prefix)
