import zipfile
import os

zip_path = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1).zip'
extract_path = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)'
files_to_restore = ['orchid-tree-website-main/index.html', 'orchid-tree-website-main/guest.html', 'orchid-tree-website-main/book-packages.html']

with zipfile.ZipFile(zip_path, 'r') as z:
    for f in files_to_restore:
        z.extract(f, extract_path)

print('Restored HTML files.')
