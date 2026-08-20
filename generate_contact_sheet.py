import os

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\images\uploads"
html_path = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\contact_sheet.html"

images = [f for f in os.listdir(base_dir) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.webp', '.svg'))]

html = """
<html>
<head>
<style>
  body { font-family: sans-serif; background: #f0f0f0; }
  .grid { display: flex; flex-wrap: wrap; gap: 20px; }
  .card { background: #fff; padding: 10px; border-radius: 8px; width: 300px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.1); }
  img { max-width: 100%; height: auto; max-height: 200px; object-fit: contain; }
  .filename { margin-top: 10px; font-size: 12px; word-break: break-all; color: #333; }
</style>
</head>
<body>
<h1>Image Contact Sheet</h1>
<p>Here are all the downloaded images and their filenames.</p>
<div class="grid">
"""

for img in images:
    html += f"""
    <div class="card">
        <img src="images/uploads/{img}" loading="lazy">
        <div class="filename">{img}</div>
    </div>
    """

html += """
</div>
</body>
</html>
"""

with open(html_path, "w", encoding="utf-8") as f:
    f.write(html)

print("Contact sheet created at contact_sheet.html")
