import os
import re

new_shorts = '''var SHORTS = [
      { lbl:'Ozone pool',                 img:'images/ozone-pool.jpg' },
      { lbl:'Farm visit',                 img:'images/uploads/farm_0K1A1757.JPG' },
      { lbl:'Bonfire & stargazing',       img:'images/uploads/bonfire.jpg' },
      { lbl:'Steam & open-sky showers',   img:'images/uploads/steam.jpg' },
      { lbl:'Karaoke & music corner',     img:'images/uploads/karaoke_0K1A7846.JPG' },
      { lbl:'Trampoline & games',         img:'images/uploads/trampoline_0K1A9822.JPG' },
      { lbl:'Birdwatching & trails',      img:'images/uploads/forest_Test-8274806.jpg' },
      { lbl:'Movies in the hall',         img:'images/uploads/movie.jpg' },
      { lbl:'Carrom',                     img:'images/uploads/chess_0K1A9971.JPG' },
      { lbl:'Kayaking',                   img:'images/uploads/kayaking_0K1A7642.JPG' },
      { lbl:'Billiards',                  img:'images/uploads/Pool_Table_74b3551af2.JPG' },
      { lbl:'Chess',                      img:'images/uploads/chess_0K1A9971.JPG' }
    ];'''

def update_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # regex to match from "var SHORTS = [" down to "];"
    content = re.sub(r'var SHORTS = \[\s*\{.*?\}\s*\];', new_shorts, content, flags=re.DOTALL)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f'Updated {filepath}')

update_file(r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\index.html')
update_file(r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\experiences.html')
