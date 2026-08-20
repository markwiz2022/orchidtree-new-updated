import os
import re

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"

def replace_in_file(filepath, pattern, replacement):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")

# 1. Update index.html
index_path = os.path.join(base_dir, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

index_pattern = r'<div class="txt">\s*<div class="eyebrow">What\'s included</div>.*?</div>\s*</div>\s*</div>\s*</section>'
index_repl = """<div class="txt">
          <div class="eyebrow">What's included</div>
          <h2>Everything you need, nothing you don't</h2>
          <p class="muted" style="margin-bottom:28px;">Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage.</p>
          <div class="incl-cols">
            <div class="incl-col in" style="border: 1px solid #d6cfc0; padding: 24px; border-radius: var(--radius-sm); background: var(--card);">
              <h3>Pradeep will provide new content for this section</h3>
              <ul>
                <li>&#10003; (Placeholder for Pradeep's content)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>"""
# The user said: "there was a 2 card in a row, you removed i understand but need to keep that and put the "Pradeep will provide new content... inside the card."
# So I should format it as a card. The original had two columns (`incl-col in` and `incl-col out`). I'll restore `incl-col in` with the placeholder.
content = re.sub(index_pattern, index_repl, content, flags=re.DOTALL)
with open(index_path, 'w', encoding='utf-8') as f:
    f.write(content)
print("Updated index.html")

# 2. Update shared/content.js
content_path = os.path.join(base_dir, "shared", "content.js")
with open(content_path, 'r', encoding='utf-8') as f:
    cjs = f.read()

cjs = re.sub(
    r'rateCovers:\s*\{[^}]*\}',
    r'''rateCovers: {
      label: "What your rate covers",
      withCredit: "Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage.",
      withoutCredit: "Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage.",
    }''',
    cjs,
    flags=re.DOTALL
)

cjs = cjs.replace(
    '"Pay the full amount shown here to confirm your booking. Nothing is due on arrival."',
    '"25% advance payment is required to confirm the booking. Guests may have the option to make full payment as well."'
)

with open(content_path, 'w', encoding='utf-8') as f:
    f.write(cjs)
print("Updated content.js")

# 3. Fix home.html links across all files
for f_name in os.listdir(base_dir):
    if f_name.endswith('.html') or f_name.endswith('.js'):
        filepath = os.path.join(base_dir, f_name)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace home.html or home.html#something with index.html
        new_content = re.sub(r'href="home\.html', r'href="index.html', content)
        new_content = re.sub(r'href=\'home\.html', r'href=\'index.html', new_content)
        new_content = re.sub(r'home\.html', r'index.html', new_content) # Just blanket replace any other occurrences.
        
        if new_content != content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"Fixed home.html links in {f_name}")
            
print("Done.")
