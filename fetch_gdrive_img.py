import urllib.request
import re
import sys
import os

url = sys.argv[1]
out_dir = sys.argv[2]
os.makedirs(out_dir, exist_ok=True)

print("Fetching folder:", url)
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
try:
    html = urllib.request.urlopen(req).read().decode('utf-8')
    
    # We look for something like "1abcd...", "filename.jpg"
    # Actually, Google Drive HTML encodes metadata. Let's look for combinations of ID and .jpg
    # Using regex to find file names ending in .jpg or .JPG and their preceding IDs
    
    # Typical pattern in gdrive html:
    # ["1mmn2...","karaoke.jpg"
    matches = re.findall(r'\[\"([a-zA-Z0-9_-]{33})\",\"([^\"]+\.(?:jpg|jpeg|png))\"', html, re.IGNORECASE)
    
    if not matches:
        # try another pattern
        matches = re.findall(r'\"([a-zA-Z0-9_-]{33})\",.*?\"([^\"]+\.(?:jpg|jpeg|png))\"', html, re.IGNORECASE)

    if not matches:
        print("No image files found in HTML.")
        sys.exit(1)
        
    print(f"Found {len(matches)} image(s).")
    
    first_id, first_name = matches[0]
    print(f"Target: {first_name} (ID: {first_id})")
    
    # Use gdown to download just this one file
    import gdown
    out_path = os.path.join(out_dir, first_name)
    gdown.download(id=first_id, output=out_path, quiet=False)
    print(f"Successfully downloaded to {out_path}")
    
except Exception as e:
    print(e)
