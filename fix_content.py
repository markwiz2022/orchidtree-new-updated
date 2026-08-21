import re

with open('shared/content.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix duplication of The Commons
content = re.sub(r'(\s*\{\s*label:\s*"The Commons / Outdoor Activities",\s*items:\s*\[[\s\S]*?\]\s*\},\s*){2,}', 
                 r'\g<1>', content)

# Remove Restaurant from Around the estate
content = re.sub(r',\s*\{\s*label:\s*"Restaurant",\s*icon:\s*"coffee"\s*\}', '', content)
content = re.sub(r'\{\s*label:\s*"Restaurant",\s*icon:\s*"coffee"\s*\},?', '', content)

with open('shared/content.js', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed content.js!')
