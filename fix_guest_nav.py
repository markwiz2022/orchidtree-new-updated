import re

with open('guest.html', 'r', encoding='utf-8') as f:
    content = f.read()

# I want to remove the specific stray lines:
# .nav { padding: 12px var(--pad); flex-direction: column; gap: 12px; }
# .nav .links { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; font-size: 10px; }
# from outside the media query.
# Let's just find and remove them if they are duplicated incorrectly.

lines = content.split('\n')
new_lines = []
in_media = False
for line in lines:
    if '@media' in line:
        in_media = True
    elif '}' in line and in_media and line.strip() == '}':
        in_media = False
    
    if not in_media:
        if '.nav { padding: 12px var(--pad); flex-direction: column; gap: 12px; }' in line:
            continue
        if '.nav .links { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; font-size: 10px; }' in line:
            continue
            
    new_lines.append(line)

with open('guest.html', 'w', encoding='utf-8') as f:
    f.write('\n'.join(new_lines))
