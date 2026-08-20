import os
import re

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"

index_path = os.path.join(base_dir, "index.html")
with open(index_path, 'r', encoding='utf-8') as f:
    content = f.read()

index_pattern = r'<div class="txt">\s*<div class="eyebrow">What\'s included</div>.*?</div>\s*</div>\s*</div>\s*</section>'

index_repl = """<div class="txt">
          <div class="eyebrow">What's included</div>
          <h2>Everything you need, nothing you don't</h2>
          <div class="incl-cols" style="margin-top:28px;">
            <div class="incl-col in">
              <h3>Included with your stay</h3>
              <ul>
                <li>All meals prepared to your preference</li>
                <li>Full access to the estate</li>
                <li>One full-body massage</li>
                <li>Traditional Kansa foot massage for accompanying guests</li>
              </ul>
            </div>
            <div class="incl-col out">
              <h3>Pradeep will provide new content for this section</h3>
              <ul>
                <li>(Placeholder for Pradeep's content)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>"""

new_content = re.sub(index_pattern, index_repl, content, flags=re.DOTALL)
if new_content != content:
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Updated index.html layout")
else:
    print("No changes made to index.html")
