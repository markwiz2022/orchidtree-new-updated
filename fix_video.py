import os

for f in ['index.html', 'guest.html']:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Replace the object-fit:cover in the video injection line
    content = content.replace(
        'object-fit:cover; position:absolute; top:0; left:0; pointer-events:none;"></video>', 
        'object-fit:contain; position:absolute; top:0; left:0; pointer-events:none;"></video>'
    )
    
    with open(f, 'w', encoding='utf-8') as file:
        file.write(content)
print('Fixed video object-fit!')
