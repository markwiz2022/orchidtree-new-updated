import os, re
filepath = 'guest.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

NAV_HTML = '''    <!-- NAV -->
    <div class="nav" id="nav">
      <a class="logo" href="index.html" aria-label="Orchid Tree home"><img src="images/logo.png" alt="Orchid Tree"></a>
      <div class="links">
        <a href="index.html">Home</a>
        <a href="stays.html">Stays</a>
        <a href="experiences.html">Experiences</a>
        <a href="weddings.html">Weddings</a>
        <a href="corporate.html">Corporate</a>
        <a href="about.html">About</a>
        <a href="https://wa.me/918088251913?text=Hi%20Orchid%20Tree%2C%20I%27d%20like%20to%20enquire%20about%20a%20stay." class="reserve" target="_blank" rel="noopener">WhatsApp</a>
      </div>
    </div>'''

if '<div id="page"' in content:
    content = content.replace('<div id="page" style="display:none;">', '<div id="page" style="display:none;">\n' + NAV_HTML)

mobile_css = '''
@media (max-width: 820px) {
  .nav { padding: 12px var(--pad); flex-direction: column; gap: 12px; }
  .nav .links { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; font-size: 10px; }
}
'''
if 'flex-wrap: wrap;' not in content:
    content = content.replace('</style>', mobile_css + '</style>')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed guest.html!')
