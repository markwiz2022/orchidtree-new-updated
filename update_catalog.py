import os
import re

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\shared\catalog.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I need to insert "images/uploads/ROOMID_vid.mp4", right after the first image in each room's imageUrls array.
room_ids = ["ashoka", "bael", "bilva", "bodhi-tree", "chandana", "datura", "mallige", "parijata", "spatika", "tulsi"]

for room in room_ids:
    # Find { id: "ROOM", name: "...", type: "...", imageUrls: [ "img1", ... ] }
    # Let's use a regex to inject it after the first string in imageUrls.
    pattern = r'({ id: "'+room+r'".*?imageUrls:\s*\[\s*("[^"]+")(,))'
    
    vid_str = f' "images/uploads/{room}_vid.mp4",'
    def repl(m):
        return m.group(1).replace(m.group(2) + m.group(3), m.group(2) + m.group(3) + vid_str)
        
    content = re.sub(pattern, repl, content, flags=re.DOTALL)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated catalog.js")
