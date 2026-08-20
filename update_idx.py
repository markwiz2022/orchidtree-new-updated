import os

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    "img:'images/uploads/Image8_scaled_jpg_ec00384f49.webp'",
    "img:'images/uploads/farm_0K1A1757.JPG'"
)
# Note: In the screenshot, Bonfire & stargazing has a lawn with 2 chairs. 
# Looking at the list, I think it was 'images/uploads/Image_6_1024x1536_bk_923d98c089.jpg' (outdoor BYOB lounge)
# Let's replace the placeholder for Bonfire.
content = content.replace(
    "{ lbl:'Bonfire & stargazing', img:'images/uploads/Experience_section_jpg_afb1c77479.webp' }",
    "{ lbl:'Bonfire & stargazing', img:'images/uploads/Image_6_1024x1536_bk_923d98c089.jpg' }"
)
content = content.replace(
    "{ lbl:'Karaoke & music corner', img:'images/uploads/Copy_of_2_a5beee287f.jpg' }",
    "{ lbl:'Karaoke & music corner', img:'images/uploads/karaoke_0K1A7846.JPG' }"
)
content = content.replace(
    "{ lbl:'Trampoline & games', img:'images/uploads/Image_6_1024x1536_bk_923d98c089.jpg' }",
    "{ lbl:'Trampoline & games', img:'images/uploads/trampoline_0K1A9822.JPG' }"
)
content = content.replace(
    "img:'images/uploads/chandana_2_00966a14a0.png'",
    "img:'images/uploads/forest_Test-8274806.jpg'"
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated index.html')

# Also update experiences.html with the new farm and forest images
exp_path = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\experiences.html'
with open(exp_path, 'r', encoding='utf-8') as f:
    exp_content = f.read()

exp_content = exp_content.replace(
    "img:'images/uploads/drive_outdoor/Goushala/Goushala 01.jpg'",
    "img:'images/uploads/farm_0K1A1757.JPG'"
)
exp_content = exp_content.replace(
    "img:'images/uploads/drive_outdoor/Forest walk/Forest walk 01.jpg'",
    "img:'images/uploads/forest_Test-8274806.jpg'"
)

with open(exp_path, 'w', encoding='utf-8') as f:
    f.write(exp_content)
print('Updated experiences.html')
