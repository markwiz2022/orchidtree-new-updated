import os

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\experiences.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# I will use replace() to update specific lines
content = content.replace(
    "{ lbl:'Karaoke & music corner',     img:'images/uploads/Copy_of_2_a5beee287f.jpg' }",
    "{ lbl:'Karaoke & music corner',     img:'images/uploads/karaoke_0K1A7846.JPG' }"
)

content = content.replace(
    "{ lbl:'Trampoline & games',         img:'images/uploads/Image_6_1024x1536_bk_923d98c089.jpg' }",
    "{ lbl:'Trampoline & games',         img:'images/uploads/trampoline_0K1A9822.JPG' }"
)

content = content.replace(
    "{ lbl:'Carrom',                     img:'images/uploads/Copy_of_2_a5beee287f.jpg' }",
    "{ lbl:'Carrom',                     img:'images/uploads/chess_0K1A9971.JPG' }"
)

content = content.replace(
    "{ lbl:'Chess',                      img:'images/uploads/tulsi_1_9846f07961.png' }",
    "{ lbl:'Chess',                      img:'images/uploads/chess_0K1A9971.JPG' }"
)

# And for kayaking, let's replace Table tennis with it since Table tennis has a placeholder
content = content.replace(
    "{ lbl:'Table tennis',               img:'images/uploads/Copy_of_2_a5beee287f.jpg' }",
    "{ lbl:'Kayaking',                   img:'images/uploads/kayaking_0K1A7642.JPG' }"
)

# Replace farm visit if it was missed
content = content.replace(
    "{ lbl:'Farm visit',    img:'images/uploads/Experience_section_jpg_afb1c77479.webp' }",
    "{ lbl:'Farm visit',    img:'images/uploads/drive_outdoor/Goushala/Goushala 01.jpg' }"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated experiences.html')
