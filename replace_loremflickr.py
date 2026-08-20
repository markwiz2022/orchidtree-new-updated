import os
import re

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\weddings.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

replacements = [
    ('https://images.unsplash.com/photo-1519741497674-611481863552?w=1600&q=80&auto=format&fit=crop', 'https://loremflickr.com/1600/900/indian,wedding,couple?random=1'),
    ('https://images.pexels.com/photos/1444442/pexels-photo-1444442.jpeg?auto=compress&cs=tinysrgb&w=900', 'https://loremflickr.com/900/600/indian,wedding,bride?random=2'),
    ('https://images.unsplash.com/photo-1522413452208-996ff3f3e740?w=900&q=80&auto=format&fit=crop', 'https://loremflickr.com/900/600/indian,wedding,groom?random=3'),
    ('https://images.unsplash.com/photo-1583939003579-730e3918a45a?w=900&q=80&auto=format&fit=crop', 'https://loremflickr.com/900/600/indian,wedding,ceremony?random=4'),
    ('https://images.unsplash.com/photo-1537633552985-df8429e8048b?w=900&q=80&auto=format&fit=crop', 'https://loremflickr.com/900/600/indian,wedding,mandap?random=5'),
    ('https://images.pexels.com/photos/265722/pexels-photo-265722.jpeg?auto=compress&cs=tinysrgb&w=600', 'https://loremflickr.com/600/400/indian,wedding,decor?random=6'),
    ('https://images.unsplash.com/photo-1465495976277-4387d4b0b4c6?w=600&q=80&auto=format&fit=crop', 'https://loremflickr.com/600/400/indian,wedding,tradition?random=7'),
    ('https://images.unsplash.com/photo-1525258946800-98cfd641d0de?w=600&q=80&auto=format&fit=crop', 'https://loremflickr.com/600/400/indian,wedding,jewelry?random=8'),
    ('https://images.pexels.com/photos/2253870/pexels-photo-2253870.jpeg?auto=compress&cs=tinysrgb&w=900', 'https://loremflickr.com/900/600/indian,wedding,dance?random=9')
]

for old_url, new_url in replacements:
    content = content.replace(old_url, new_url)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated weddings.html with loremflickr images!")
