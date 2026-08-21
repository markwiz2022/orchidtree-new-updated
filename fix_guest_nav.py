import os, re

target_css = '''
.nav{position:fixed;top:0;left:0;right:0;z-index:90;display:flex;align-items:center;justify-content:space-between;padding:24px var(--pad);background:linear-gradient(to bottom,rgba(20,16,12,.55),rgba(20,16,12,0));transition:background .3s ease,padding .3s ease,box-shadow .3s ease;}
.nav .logo{display:flex;align-items:center;}
.nav .logo img{height:72px;width:auto;display:block;filter:brightness(0) invert(1) drop-shadow(0 1px 6px rgba(0,0,0,.4));transition:height .3s ease,filter .3s ease;}
.nav.solid .logo img{height:52px;filter:none;}
.nav .links{display:flex;gap:30px;align-items:center;font-size:11px;letter-spacing:2.5px;text-transform:uppercase;font-weight:600;}
.nav .links a{color:rgba(255,255,255,.9);text-decoration:none;text-shadow:0 1px 8px rgba(0,0,0,.45);transition:opacity .2s ease,color .3s ease,text-shadow .3s ease;}
.nav .links a:not(.reserve){position:relative;}
.nav .links a:not(.reserve)::after{content:"";position:absolute;left:2px;right:2px;bottom:-5px;height:1.5px;background:currentColor;transform:scaleX(0);transform-origin:left;transition:transform .28s ease;}
.nav .links a:not(.reserve):hover::after{transform:scaleX(1);}
.nav .links a:hover{opacity:1;}
.nav .links .reserve{border:1px solid rgba(255,255,255,.6);padding:9px 18px;border-radius:var(--radius-sm);transition:all .2s ease;}
.nav .links .reserve:hover{background:#fff;color:var(--ink);opacity:1;}
.nav.solid{background:rgba(247,243,234,.96);box-shadow:0 2px 22px rgba(67,56,43,.09);padding-top:15px;padding-bottom:15px;backdrop-filter:blur(6px);}
.nav.solid .links a{color:var(--ink);text-shadow:none;}
.nav.solid .links .reserve{border-color:var(--green);color:var(--green);}
.nav.solid .links .reserve:hover{background:var(--green);color:#fff;}
@media (max-width: 820px) {
  .nav { padding: 12px var(--pad); flex-direction: column; gap: 12px; }
  .nav .links { display: flex; flex-wrap: wrap; justify-content: center; gap: 15px; font-size: 10px; }
}
'''

scroll_js = '''
<script>
window.addEventListener('scroll', function() {
    var nav = document.getElementById('nav');
    if (nav) {
        if (window.scrollY > 50) {
            nav.classList.add('solid');
        } else {
            nav.classList.remove('solid');
        }
    }
});
</script>
'''

with open('guest.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('<style>', '<style>\n' + target_css.strip() + '\n', 1)

if "window.addEventListener('scroll'" not in content:
    content = content.replace('</body>', scroll_js + '\n</body>')

with open('guest.html', 'w', encoding='utf-8') as f:
    f.write(content)
print('Fixed guest.html nav CSS and JS!')
