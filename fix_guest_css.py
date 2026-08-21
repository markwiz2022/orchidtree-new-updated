import os

css_to_add = '''
.nav {
  position: fixed; top: 0; left: 0; right: 0; z-index: 90;
  display: flex; align-items: center; justify-content: space-between;
  padding: 15px var(--pad);
  background: rgba(247,243,234,1); /* solid beige */
  box-shadow: 0 2px 22px rgba(67,56,43,.09);
}
.nav .logo { display: flex; align-items: center; }
.nav .logo img { height: 52px; width: auto; display: block; }
.nav .links {
  display: flex; gap: 30px; align-items: center;
  font-size: 11px; letter-spacing: 2.5px; text-transform: uppercase; font-weight: 600;
}
.nav .links a {
  color: var(--ink); text-decoration: none; transition: opacity .2s ease, color .3s ease;
}
.nav .links a:not(.reserve) { position: relative; }
.nav .links a:not(.reserve)::after {
  content: ""; position: absolute; left: 2px; right: 2px; bottom: -5px; height: 1.5px;
  background: currentColor; transform: scaleX(0); transform-origin: left; transition: transform .28s ease;
}
.nav .links a:not(.reserve):hover::after { transform: scaleX(1); }
.nav .links .reserve {
  border: 1px solid var(--green); color: var(--green);
  padding: 9px 18px; border-radius: var(--radius-sm); transition: all .2s ease;
}
.nav .links .reserve:hover { background: var(--green); color: #fff; }

@media (max-width: 820px) {
  .nav { padding: 12px var(--pad); flex-direction: column; gap: 12px; }
  .nav .links { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; font-size: 10px; }
}
'''

with open('guest.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert after <style>
content = content.replace('<style>', '<style>\n' + css_to_add, 1)

with open('guest.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Added clean nav CSS to guest.html')
