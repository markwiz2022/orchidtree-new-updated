import os

with open('corporate.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace(
    '<img src="images/uploads/Experience_section_jpg_afb1c77479.webp" alt="Open-air breakout corners among the trees at Orchid Tree estate"',
    '<img src="images/uploads/corporate_outdoor.jpg" alt="Open-air breakout corners among the trees at Orchid Tree estate"'
)

with open('corporate.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated corporate.html with new image')
