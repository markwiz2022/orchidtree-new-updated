import os, re

new_shorts = '''var SHORTS = [
{ lbl:'Ozone Pool',                 img:'images/ozone-pool.jpg' },
{ lbl:'Steam Room',                 img:'images/uploads/steam.jpg' },
{ lbl:'Head Massage',               img:'', slot:'Head Massage' },
{ lbl:'Leg Massage',                img:'images/uploads/kansa.jpg' },
{ lbl:'Farm Visit',                 img:'images/uploads/farm_0K1A1757.JPG' },
{ lbl:'Meet Our Pets',              img:'', slot:'Meet Our Pets' },
{ lbl:'Bonfire',                    img:'images/uploads/bonfire.jpg' },
{ lbl:'Stargazing',                 img:'', slot:'Stargazing' },
{ lbl:'Bird Watching',              img:'images/uploads/forest_Test-8274806.jpg' },
{ lbl:'Anniversary Celebration',    img:'', slot:'Anniversary Celebration' },
{ lbl:'Birthday Celebration',       img:'images/uploads/bday celeb.jpeg' },
{ lbl:'Billiards',                  img:'images/uploads/Pool_Table_74b3551af2.JPG' },
{ lbl:'Trampoline',                 img:'images/uploads/trampoline_0K1A9822.JPG' },
{ lbl:'Movie in the Hall',          img:'images/uploads/movie.jpg' },
{ lbl:'Karaoke',                    img:'images/uploads/karaoke_0K1A7846.JPG' },
{ lbl:'Chess',                      img:'images/uploads/chess.jpg' },
{ lbl:'Carrom',                     img:'images/uploads/carrom.jpg' },
{ lbl:'Book Reading',               img:'', slot:'Book Reading' }
];
document.getElementById('expShorts').innerHTML = SHORTS.map(function(s){
if(s.img){
return '<div class="short" aria-label="'+esc(s.lbl)+'"><div class="ph" style="background-image:url(\\''+esc(s.img)+'\\')"></div><div class="scrim"></div><div class="lbl">'+esc(s.lbl)+'</div></div>';
}
return '<div class="short placeholder" aria-label="'+esc(s.lbl)+'" data-slot="'+esc(s.slot)+'"><div class="ph"></div><div class="slot-tag">Photo: '+esc(s.slot)+'</div><div class="scrim"></div><div class="lbl">'+esc(s.lbl)+'</div></div>';
}).join('');'''

with open('index.html', 'r', encoding='utf-8') as f: content = f.read()
content = re.sub(r'var SHORTS = \[.*?\}\n\];\ndocument\.getElementById\(\'expShorts\'\)\.innerHTML = SHORTS\.map\(function\(s\)\{.*?\n\}\)\.join\(\'\'\);', new_shorts, content, flags=re.DOTALL)
with open('index.html', 'w', encoding='utf-8') as f: f.write(content)

with open('experiences.html', 'r', encoding='utf-8') as f: content = f.read()
content = re.sub(r'var SHORTS = \[.*?\}\n\];\ndocument\.getElementById\(\'expShorts\'\)\.innerHTML = SHORTS\.map\(function\(s\)\{.*?\n\}\)\.join\(\'\'\);', new_shorts, content, flags=re.DOTALL)
with open('experiences.html', 'w', encoding='utf-8') as f: f.write(content)

print("Updated SHORTS in index and experiences")
