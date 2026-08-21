import os

for f in ['index.html', 'experiences.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    content = content.replace("{ lbl:'Carrom',                     img:'images/uploads/chess_0K1A9971.JPG' }", "{ lbl:'Carrom',                     img:'images/uploads/carrom.jpg' }")
    content = content.replace("{ lbl:'Chess',                      img:'images/uploads/chess_0K1A9971.JPG' }", "{ lbl:'Chess',                      img:'images/uploads/chess.jpg' }")
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Fixed chess and carrom paths!')
