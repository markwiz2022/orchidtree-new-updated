import os
import re

base_dir = r"C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main"

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

html_files = [f for f in os.listdir(base_dir) if f.endswith('.html')]

for f in html_files:
    filepath = os.path.join(base_dir, f)
    with open(filepath, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # 1. Remove ANY `<div class="nav"...>` blocks
    content = re.sub(r'<!-- NAV -->\s*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<!-- NAV \(.*?\) -->\s*', '', content, flags=re.IGNORECASE)
    content = re.sub(r'<div class="nav(?:[^>]*)".*?</div>\s*</div>', '', content, flags=re.DOTALL)
    
    # 2. Remove ANY `<nav class="nav"...>` blocks, sometimes wrapped in <header>
    content = re.sub(r'<header>\s*<nav class="nav(?:[^>]*)".*?</nav>\s*</header>', '', content, flags=re.DOTALL)
    content = re.sub(r'<nav class="nav(?:[^>]*)".*?</nav>', '', content, flags=re.DOTALL)
    
    # Also fix broken image links like href="home.html" that might be around
    content = content.replace('href="home.html"', 'href="index.html"')
    
    # Insert new nav right after <body> or <div id="page"...>
    if '<div id="page"' in content:
        content = content.replace('<div id="page" style="display:none;">', '<div id="page" style="display:none;">\n' + NAV_HTML)
    else:
        content = content.replace('<body>', '<body>\n' + NAV_HTML)
        
    with open(filepath, 'w', encoding='utf-8') as file:
        file.write(content)
        
print("Headers fixed.")
