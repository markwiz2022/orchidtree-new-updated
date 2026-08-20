import os
import re

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"

def replace_in_file(filepath, pattern, replacement):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    new_content = re.sub(pattern, replacement, content, flags=re.IGNORECASE | re.DOTALL)
    if new_content != content:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {os.path.basename(filepath)}")

# --- Task 1, 2, 3: Update catalog.js ---
catalog_path = os.path.join(base_dir, "shared", "catalog.js")
with open(catalog_path, 'r', encoding='utf-8') as f:
    cat = f.read()

# Task 1: Couple rooms -> American Standard Queen Size Bed
cat = cat.replace('{ label: "Bed", value: "One king bed" }', '{ label: "Bedding", value: "American Standard Queen Size Bed" }')
# Task 2: Family room by the pool -> King Bed + Queen Size Pull-Out Bed
cat = cat.replace('{ label: "Bedding", value: "King bed with pull-out bedding" }', '{ label: "Bedding", value: "King Bed + Queen Size Pull-Out Bed" }')

# Task 3: Room-specific info
# Find `facts: t.facts.slice(),` and replace it with dynamic facts
injection = """      facts: (function() {
        let f = t.facts.slice();
        if (r.id === "mallige" || r.id === "spatika") f.push({ label: "Features", value: "Walk-in Wardrobe + Contemporary Bedding" });
        if (r.id === "ashoka") f.push({ label: "Features", value: "Skylight Bath" });
        if (r.id === "parijata") f.push({ label: "Features", value: "Spacious Bath" });
        return f;
      })(),"""
cat = cat.replace("facts: t.facts.slice(),", injection)

with open(catalog_path, 'w', encoding='utf-8') as f:
    f.write(cat)
print("Updated catalog.js")

# --- Task 8, 9, 10, 14, 15, 16: content.js ---
content_path = os.path.join(base_dir, "shared", "content.js")
with open(content_path, 'r', encoding='utf-8') as f:
    cont = f.read()

# Task 8, 9, 10
cont = cont.replace('"Your booking is confirmed once the full amount is paid on this page."', '"25% advance payment is required to confirm the booking. Guests may have the option to make full payment as well.",\n            "Your booking is confirmed once the advance is paid.",\n            "Pradeep will share the final Terms & Conditions content."')

# Task 14: Add Facilities
if "Swimming Pool" not in cont:
    cont = cont.replace('facilitiesSection: {', 'facilitiesSection: {\n      additional: ["Swimming Pool", "Steam Room", "Massage", "Billiards"],')

# Task 15, 16
around_estate = """        { label: "The Commons / Outdoor Activities", items: [
          { label: "Football", icon: "ball" },
          { label: "Volleyball", icon: "ball" },
          { label: "Cricket", icon: "bat" }
        ] },
        { label: "Around the estate", items: [
          { label: "Estate Farm Visit — approximately 1 km away", icon: "leaf" },
          { label: "Jungle Walk", icon: "trail" },
          { label: "Banyan Tree Visit", icon: "leaf" },
          { label: "Restaurant", icon: "coffee" }
        ] }"""
# Replace the existing "Around the estate" array
cont = re.sub(r'\{\s*label:\s*"Around the estate",\s*items:\s*\[.*?\]\s*\}', around_estate, cont, flags=re.DOTALL)

# Remove "Buggy" from content.js
cont = re.sub(r'\{\s*label:\s*"Buggy ride to the farm",.*?\},\s*', '', cont)

with open(content_path, 'w', encoding='utf-8') as f:
    f.write(cont)
print("Updated content.js")

# --- Task 13: Remove "Buggy" everywhere ---
buggy_replacements = [
    (r'Take the buggy down to the farm and pull a tomato off the vine\.', r'Visit the farm and pull a tomato off the vine.'),
    (r'farm and buggy rides', 'farm visits'),
    (r'visit the farm and take a buggy ride', 'visit the farm'),
    (r'take a buggy ride to the farm', 'visit the farm'),
    (r'Farm visit & buggy ride', 'Farm visit'),
    (r'the farm and buggy', 'the farm')
]

# --- Task 8: Advance payment in FAQs ---
faq_replacements = [
    (r'You pay the full amount shown to confirm your booking\. Nothing is due on arrival\.', '25% advance payment is required to confirm the booking. Guests may have the option to make full payment as well.'),
]

# --- Tasks 4, 17, 18: Navigation ---
NAV_HTML = """    <!-- NAV -->
    <div class="nav" id="nav">
      <a class="logo" href="index.html" aria-label="Orchid Tree home"><img src="images/logo.png" alt="Orchid Tree"></a>
      <div class="links">
        <a href="stays.html">Stays</a>
        <a href="experiences.html">Experiences</a>
        <a href="weddings.html">Weddings</a>
        <a href="corporate.html">Corporate</a>
        <a href="about.html">About</a>
        <a href="https://wa.me/918088251913?text=Hi%20Orchid%20Tree%2C%20I%27d%20like%20to%20enquire%20about%20a%20stay." class="reserve" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>"""

# --- Task 11, 12: index.html specific ---
index_incl_pattern = r'<div class="txt">\s*<div class="eyebrow">What\'s included</div>.*?</div>\s*</div>\s*</section>'
index_incl_replacement = """<div class="txt">
          <div class="eyebrow">What's included</div>
          <h2>Everything you need, nothing you don't</h2>
          <p class="muted" style="margin-bottom:28px;">Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage.</p>
          <div class="incl-cols">
            <div class="incl-col in">
              <h3>Pradeep will provide new content for this section</h3>
              <ul>
                <li>(Placeholder for Pradeep's content)</li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </section>"""

html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]
for html_file in html_files:
    filepath = os.path.join(base_dir, html_file)
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    orig = content
    
    # Buggy replacements
    for p, r in buggy_replacements:
        content = re.sub(p, r, content, flags=re.IGNORECASE)
    
    # FAQ replacements
    for p, r in faq_replacements:
        content = re.sub(p, r, content, flags=re.IGNORECASE)
        
    # Remove restaurant from footer
    content = re.sub(r'<a href="restaurant\.html">Restaurant</a>', '', content, flags=re.IGNORECASE)
    
    # Navigation rewrite
    # Find existing <div class="nav"...> ... </div> block and replace it
    # Note: guest.html doesn't have it, so insert after <body>
    nav_match = re.search(r'<div class="nav(?:[^>]*)".*?</div>\s*</div>', content, flags=re.DOTALL)
    if nav_match:
        # Check if it has <a class="logo" inside.
        if '<a class="logo"' in nav_match.group(0):
            content = content[:nav_match.start()] + NAV_HTML + content[nav_match.end():]
    else:
        # No nav found (like guest.html). Insert after <body> or <div id="page"...>
        if '<div id="page"' in content:
            content = content.replace('<div id="page" style="display:none;">', '<div id="page" style="display:none;">\n' + NAV_HTML)
        else:
            content = content.replace('<body>', '<body>\n' + NAV_HTML)
            
    # If index.html, do Task 11, 12
    if html_file == 'index.html':
        content = re.sub(index_incl_pattern, index_incl_replacement, content, flags=re.DOTALL)
        
    if content != orig:
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f"Updated {html_file}")

print("All tasks completed.")
