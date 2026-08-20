import os, glob, re

dir_path = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main'

for file in glob.glob(os.path.join(dir_path, '*.html')):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    if ':root' in content and '--pad:' not in content:
        content = re.sub(r'(:root\s*\{[^}]*)(\})', r'\1  --pad:clamp(24px,6.5vw,110px);\n\2', content, count=1)
        
        with open(file, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Added --pad to {os.path.basename(file)}")
