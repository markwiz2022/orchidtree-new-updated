import os
import re

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"

# Manual mapping for specific things based on user requests
# We know the live images are stored in images/uploads/...
# 1. Trampoline -> Image_6_1024x1536_bk_923d98c089.jpg
# 2. Outdoor Games -> Image8_scaled_jpg_ec00384f49.webp (assumption for games/outdoor)
# 3. Movies/Theater -> Copy_of_2_a5beee287f.jpg
# 4. Conference/Meeting -> K1_A1612_scaled_d35379acb2.jpg
# 5. Wedding -> K1_A1497_934d9aad84.jpg (or something else, but let's just replace unsplash with real ones)

mapping = {
    # In experiences.html
    "images/uploads/chandana_2_00966a14a0.png": "images/uploads/Image_6_1024x1536_bk_923d98c089.jpg", # Trampoline fix
    "images/uploads/bael_1_2b4731913c.png": "images/uploads/Image8_scaled_jpg_ec00384f49.webp", # Carrom/Games fix
    "images/uploads/bodhi_tree_3_png_eedb89acdf.webp": "images/uploads/Copy_of_0_K1_A1497_934d9aad84.jpg", # Birdwatching fix
    "images/uploads/chandana_3_b67610e6cf.png": "images/uploads/chandana_3_b67610e6cf.png", # Keep Chandana room
    
    # Generic Unsplash replacements (We will just do a regex replace)
}

# 1. Fix specific incorrect images in experiences.html
exp_path = os.path.join(base_dir, "experiences.html")
with open(exp_path, "r", encoding="utf-8") as f:
    exp_content = f.read()

# Replace the wrong room images being used for activities
exp_content = exp_content.replace("{ lbl:'Trampoline & games',         img:'images/uploads/chandana_2_00966a14a0.png' }", "{ lbl:'Trampoline & games',         img:'images/uploads/Image_6_1024x1536_bk_923d98c089.jpg' }")
exp_content = exp_content.replace("{ lbl:'Carrom',                     img:'images/uploads/bael_1_2b4731913c.png' }", "{ lbl:'Carrom',                     img:'images/uploads/Image8_scaled_jpg_ec00384f49.webp' }")
exp_content = exp_content.replace("{ lbl:'Birdwatching & trails',      img:'images/uploads/bodhi_tree_3_png_eedb89acdf.webp' }", "{ lbl:'Birdwatching & trails',      img:'images/uploads/Copy_of_0_K1_A1497_934d9aad84.jpg' }")

with open(exp_path, "w", encoding="utf-8") as f:
    f.write(exp_content)
print("Updated experiences.html")

# 2. Scrape and replace ALL Unsplash images in all files
# We will just replace any https://images.unsplash.com/... with a random generic image from the live site, or specifically for weddings/corporate.
wedding_imgs = [
    "images/uploads/Copy_of_0_K1_A1497_934d9aad84.jpg",
    "images/uploads/Image11_5a2a5d7fce.jpg"
]
corp_imgs = [
    "images/uploads/K1_A1612_scaled_d35379acb2.jpg",
    "images/uploads/K1_A2025_scaled_jpg_b528c00060.webp",
    "images/uploads/K1_A1936_scaled_1ff342ae00.jpg",
    "images/uploads/K1_A1830_scaled_jpg_d131e68a29.webp"
]
generic_imgs = [
    "images/uploads/12_4d2f93289f.jpg",
    "images/uploads/Image8_scaled_jpg_ec00384f49.webp",
    "images/uploads/Copy_of_Pool_37_958d54313f.jpg"
]

def replace_unsplash_in_file(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        content = f.read()
    
    # We will find all unsplash URLs and replace them
    # Because there are many, let's just cycle through our real images
    urls = re.findall(r'https://images.unsplash.com/[^\s\'"<>]+', content)
    urls = list(set(urls)) # unique
    if not urls: return
    
    for i, url in enumerate(urls):
        # Decide which list to pull from based on filename
        if 'wedding' in filepath.lower():
            replacement = wedding_imgs[i % len(wedding_imgs)]
        elif 'corporate' in filepath.lower() or 'host' in filepath.lower():
            replacement = corp_imgs[i % len(corp_imgs)]
        else:
            replacement = generic_imgs[i % len(generic_imgs)]
        
        content = content.replace(url, replacement)
        
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Replaced {len(urls)} unsplash placeholders in {os.path.basename(filepath)}")

for f_name in os.listdir(base_dir):
    if f_name.endswith(".html") or f_name.endswith(".js"):
        replace_unsplash_in_file(os.path.join(base_dir, f_name))
