import os
filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\experiences.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("{ lbl:'Farm visit',                 img:'images/uploads/Experience_section_jpg_afb1c77479.webp' }", "{ lbl:'Farm visit',                 img:'images/uploads/drive_outdoor/Goushala/Goushala 01.jpg' }")
content = content.replace("{ lbl:'Birdwatching & trails',      img:'images/uploads/Copy_of_0_K1_A1497_934d9aad84.jpg' }", "{ lbl:'Birdwatching & trails',      img:'images/uploads/drive_outdoor/Forest walk/Forest walk 01.jpg' }")
content = content.replace("{ lbl:'Birdwatching & trails',      img:'images/uploads/bodhi_tree_3_png_eedb89acdf.webp' }", "{ lbl:'Birdwatching & trails',      img:'images/uploads/drive_outdoor/Forest walk/Forest walk 01.jpg' }")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
