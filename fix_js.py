import os

def fix_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    bad_str = "return '<div class=\"th' + (i === 0 ? ' active' : '') + '\" data-i=\"' + i + '\" style=\"background-image:url('' + esc(u) + '')\"></div>';"
    good_str = "return '<div class=\"th' + (i === 0 ? ' active' : '') + '\" data-i=\"' + i + '\" style=\"background-image:url(\\'' + esc(u) + '\\')\"></div>';"
    
    if bad_str in content:
        content = content.replace(bad_str, good_str)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed', filepath)
    else:
        print('Not found in', filepath)

base_dir = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main'
for f in ['index.html', 'guest.html', 'book-packages.html', 'weddings.html']:
    fix_file(os.path.join(base_dir, f))
