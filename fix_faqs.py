import os
import re

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"

new_content_text = "Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage."

for f_name in os.listdir(base_dir):
    if f_name.endswith('.html'):
        filepath = os.path.join(base_dir, f_name)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace FAQ "What's included in the price?"
        content = re.sub(
            r'(<div class="faq-item"><button class="faq-q">What\'s included in the price\?<span class="plus">\+</span></button><div class="faq-a"><p>).*?(</p></div></div>)',
            rf'\1{new_content_text}\2',
            content,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        # Replace FAQ "Is Orchid Tree all-inclusive?"
        content = re.sub(
            r'(<div class="faq-item"><button class="faq-q">Is Orchid Tree all-inclusive\?<span class="plus">\+</span></button><div class="faq-a"><p>).*?(</p></div></div>)',
            rf'\1{new_content_text}\2',
            content,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        # Replace FAQ "Is breakfast included with a stay?"
        content = re.sub(
            r'(<div class="faq-item open"><button class="faq-q">Is breakfast included with a stay\?<span class="plus">\+</span></button><div class="faq-a"><p>).*?(</p></div></div>)',
            rf'\1{new_content_text}\2',
            content,
            flags=re.IGNORECASE | re.DOTALL
        )
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Checked {f_name}")

print("Done.")
