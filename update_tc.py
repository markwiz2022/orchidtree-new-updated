import os
import re

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\shared\content.js'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

new_policies = '''    policies: [
      "Your booking is confirmed once the full amount is paid on this page.",
      "Full refund if cancelled 48 hours or more before check-in. No refund after that.",
      "Couple Rooms sleep 2 adults + 1 child up to 8 years, on one queen bed. No extra bed.",
      "Plated meals only. No outside food. No room service.",
      "We do not sell alcohol. Personal beverages only in designated areas.",
      "Pets are welcome only in pet-friendly rooms and must be leashed in common areas."
    ],'''

content = re.sub(r'policies:\s*\[.*?\]\s*,', new_policies, content, flags=re.DOTALL)

new_terms = '''    terms: {
      sections: [
        { title: "Terms and conditions", items: [
          "Your booking is confirmed once the full amount is paid on this page.",
          "Full refund if cancelled 48 hours or more before check-in. No refund after that.",
          "Couple Rooms sleep 2 adults + 1 child up to 8 years, on one queen bed. No extra bed.",
          "Plated meals only. No outside food. No room service.",
          "We do not sell alcohol. Personal beverages only in designated areas.",
          "Pets are welcome only in pet-friendly rooms and must be leashed in common areas."
        ] }
      ],
    },'''

# The original regex for terms might fail because of the trailing `},` in my pattern
# Let's just do a simpler replace for terms
content = re.sub(r'terms:\s*\{\s*sections:\s*\[.*?\]\s*\}\s*,?\s*\},', new_terms, content, flags=re.DOTALL)

# Let me check if terms is correctly replaced. If the original was just `terms: { sections: [ ... ] },`
content = re.sub(r'terms:\s*\{\s*sections:\s*\[[^\]]*\]\s*\}\s*\},', new_terms, content, flags=re.DOTALL)
content = re.sub(r'terms:\s*\{\s*sections:\s*\[.*?\]\s*\}\s*,\s*\},', new_terms, content, flags=re.DOTALL)
# Actually let's just do string replace on what I know is there

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Updated content.js')
