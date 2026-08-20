import os

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\corporate.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<video src="images/uploads/corp_vid_cisco.mp4" autoplay muted loop playsinline style="width:100%; height:100%; object-fit:cover;"></video>', '<img src="images/uploads/corp_img_cisco_output.jpg" alt="Cisco Corporate Offsite" style="width:100%; height:100%; object-fit:cover;">')
content = content.replace('<video src="images/uploads/corp_vid_sap.mp4" autoplay muted loop playsinline style="width:100%; height:100%; object-fit:cover;"></video>', '<img src="images/uploads/corp_img_sap.jpg" alt="SAP Corporate Offsite" style="width:100%; height:100%; object-fit:cover;">')
content = content.replace('<video src="images/uploads/corp_vid_sagar.mp4" autoplay muted loop playsinline style="width:100%; height:100%; object-fit:cover;"></video>', '<img src="images/uploads/corp_img_sagar.jpg" alt="Sagar Partners Corporate Offsite" style="width:100%; height:100%; object-fit:cover;">')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated corporate.html')
