import os
import re

new_text = "Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage."

for f_name in os.listdir('.'):
    if f_name.endswith('.html'):
        with open(f_name, 'r', encoding='utf-8') as f:
            content = f.read()
        
        orig = content
        
        # specific fix for experiences.html
        if 'Your room, breakfast each morning' in content:
            content = re.sub(
                r'(<div class="faq-a"><p>).*?(Lunch, dinner and a massage can be added separately\.</p>)',
                rf'\1{new_text}</p>',
                content,
                flags=re.IGNORECASE | re.DOTALL
            )
            
        if orig != content:
            with open(f_name, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f'Updated {f_name}')
