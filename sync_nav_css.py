import os, glob

target_css = '''  .nav{position:fixed;top:0;left:0;right:0;z-index:90;display:flex;align-items:center;justify-content:space-between;padding:24px var(--pad);background:linear-gradient(to bottom,rgba(20,16,12,.55),rgba(20,16,12,0));transition:background .3s ease,padding .3s ease,box-shadow .3s ease;}
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
  .nav.solid .links .reserve:hover{background:var(--green);color:#fff;}'''

dir_path = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main'

for file in glob.glob(os.path.join(dir_path, '*.html')):
    with open(file, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    new_lines = []
    for line in lines:
        if line.lstrip().startswith('.nav{position:fixed') or line.lstrip().startswith('.nav .logo') or \
           line.lstrip().startswith('.nav.solid') or (line.lstrip().startswith('.nav .links') and not 'display:none' in line) or \
           line.lstrip().startswith('.nav .'):
            continue
        new_lines.append(line)
        
    # Now insert the target_css right before </style>
    final_lines = []
    for line in new_lines:
        if '</style>' in line:
            final_lines.append(target_css + '\n')
            final_lines.append(line)
        else:
            final_lines.append(line)

    with open(file, 'w', encoding='utf-8') as f:
        f.writelines(final_lines)
    print(f"Updated {os.path.basename(file)}")
