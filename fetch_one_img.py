import urllib.request
import re
import sys
import os
import gdown

def download_first_jpg(url, name_prefix):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        
        # In Google Drive folder HTML, the file name and ID often appear together or nearby.
        # But we found the ID is in an ssk attribute near the aria-label with the file name.
        # Example: aria-label="0K1A7903.JPG Image Shared" ... ssk='5:auSv138:17BgUvuAAJDoMyMNNMdIe6spZKuxSpCsV-0-16'
        
        matches = re.findall(r'aria-label=\"([^\"]+\.(?:JPG|jpg|jpeg|png))\s+Image.*?ssk=\'\d+:[a-zA-Z0-9]+:([a-zA-Z0-9_-]{33})', html)
        
        if not matches:
            # Try a broader regex
            matches = re.findall(r'([^\"]+\.(?:JPG|jpg|jpeg|png))[^<]*?([a-zA-Z0-9_-]{33})', html)
            
        if not matches:
            print(f"No JPG found in {url}")
            return
            
        print(f"Found {len(matches)} matches for {name_prefix}.")
        filename, file_id = matches[0]
        
        # If it happens to be the folder ID, let's filter it out (folder ID is often 33 chars too)
        folder_id_match = re.search(r'folders/([a-zA-Z0-9_-]{33})', url)
        folder_id = folder_id_match.group(1) if folder_id_match else None
        
        for name, fid in matches:
            if fid != folder_id:
                filename, file_id = name, fid
                break
                
        print(f"Target: {filename} -> ID: {file_id}")
        
        out_path = f"images/uploads/{name_prefix}_{filename}"
        gdown.download(id=file_id, output=out_path, quiet=True)
        print(f"Downloaded {out_path}")
        return out_path
    except Exception as e:
        print(f"Error on {url}: {e}")

if __name__ == '__main__':
    # URLs provided
    links = [
        ("trampoline", "https://drive.google.com/drive/folders/1Itedft_oGuCAn-et53MuvdNbLlPGSrVE"),
        ("chess", "https://drive.google.com/drive/folders/1XELWapUUZxS8L6XVZeM49ZPrqTpNzVp_"),
        ("kayaking", "https://drive.google.com/drive/folders/12pGGvHfYhn22UwZNw4zs33XYJsuckn7V"),
        ("karaoke", "https://drive.google.com/drive/folders/1mmn2kBzAzSUo3GMIFNxo68r4pYQNqhbp")
    ]
    
    for prefix, url in links:
        download_first_jpg(url, prefix)
