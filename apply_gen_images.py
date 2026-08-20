import os
import re

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\weddings.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('https://images.unsplash.com/photo-1519741497674-611481863552?w=1600&q=80&auto=format&fit=crop', 'images/uploads/gen_wedding_hero.jpg'),
    ('https://loremflickr.com/900/600/indian,wedding?lock=20', 'images/uploads/gen_wedding_couple.jpg'),
    ('https://images.unsplash.com/photo-1522413452208-996ff3f3e740?w=900&q=80&auto=format&fit=crop', 'images/uploads/gen_wedding_ritual.jpg'),
    ('https://loremflickr.com/900/600/indian,wedding,couple?lock=10', 'images/uploads/gen_wedding_wide.jpg'),
    ('https://images.unsplash.com/photo-1537633552985-df8429e8048b?w=900&q=80&auto=format&fit=crop', 'images/uploads/gen_wedding_hero.jpg'),
    ('https://images.pexels.com/photos/265722/pexels-photo-265722.jpeg?auto=compress&cs=tinysrgb&w=600', 'images/uploads/gen_wedding_couple.jpg'),
    ('https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?w=600&q=80&auto=format&fit=crop', 'images/uploads/gen_wedding_ritual.jpg'),
    ('https://images.unsplash.com/photo-1525258946800-98cfd641d0de?w=600&q=80&auto=format&fit=crop', 'images/uploads/gen_wedding_wide.jpg'),
    ('https://images.pexels.com/photos/2253870/pexels-photo-2253870.jpeg?auto=compress&cs=tinysrgb&w=900', 'images/uploads/gen_wedding_couple.jpg')
]

for old_url, new_url in replacements:
    content = content.replace(old_url, new_url)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated weddings.html with AI generated images!")
