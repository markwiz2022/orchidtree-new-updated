import urllib.request
import re

def get_jpg_from_folder(url):
    req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    try:
        html = urllib.request.urlopen(req).read().decode('utf-8')
        # Google drive folder HTML contains JSON data with file IDs and names
        # Usually looking for file ID, file name, etc.
        # Let's just find anything ending in .JPG or .jpg and the ID nearby
        print(len(html))
        # Find all 33-character IDs
        ids = re.findall(r'\"([a-zA-Z0-9_-]{33})\"', html)
        print("IDs found:", len(ids))
        
        # We can just write a quick script using gdown python API
        import gdown
        import gdown.folder
        
        # gdown has download_folder, but what if we just parse the folder?
        # gdown.download_folder returns a list of downloaded files, but it downloads them.
        
    except Exception as e:
        print(e)

get_jpg_from_folder('https://drive.google.com/drive/folders/1Itedft_oGuCAn-et53MuvdNbLlPGSrVE')
