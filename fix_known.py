import os
filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\experiences.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace("{ lbl:'Billiards',                  img:'images/uploads/spatika_1_5f0d445b7b.png' }", "{ lbl:'Billiards',                  img:'images/uploads/Pool_Table_74b3551af2.JPG' }")
content = content.replace("{ lbl:'Carrom',                     img:'images/uploads/Image8_scaled_jpg_ec00384f49.webp' }", "{ lbl:'Carrom',                     img:'images/uploads/Copy_of_2_a5beee287f.jpg' }")
content = content.replace("{ lbl:'Carrom',                     img:'images/uploads/bael_1_2b4731913c.png' }", "{ lbl:'Carrom',                     img:'images/uploads/Copy_of_2_a5beee287f.jpg' }")

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("done")
