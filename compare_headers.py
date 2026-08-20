import os
def get_header(file):
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
        start = content.find('<div class="nav"')
        if start == -1:
            start = content.find('<nav>')
        if start != -1:
            end = content.find('</div>', start)
            end = content.find('</div>', end + 6) # one level deep
            return content[start:end+6]
    return "Not found"

print('--- index.html ---')
print(get_header(r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\index.html'))
print('\n--- guest.html ---')
print(get_header(r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\guest.html'))
