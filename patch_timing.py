import os
import re

new_mg_code = '''function mgLayers(){ return [document.querySelector('#mMain .rm-base'), document.querySelector('#mMain .rm-top')]; }
    function setLayer(layer, url) {
      if (url && (url.toLowerCase().endsWith('.mp4') || url.toLowerCase().endsWith('.webm'))) {
        layer.style.backgroundImage = 'none';
        layer.innerHTML = '<video src="'+url+'" autoplay muted playsinline style="width:100%; height:100%; object-fit:cover; position:absolute; top:0; left:0; pointer-events:none;"></video>';
        return layer.querySelector('video');
      } else {
        layer.innerHTML = '';
        layer.style.backgroundImage = url ? "url('" + url + "')" : '';
        return null;
      }
    }
    function mgGo(target){
      var n = MG.urls.length; if(!n) return;
      target = (target + n) % n; MG.i = target;
      var layers = mgLayers(), incoming = layers[1 - MG.cur];
      var vid = setLayer(incoming, MG.urls[target]);
      incoming.style.opacity = '1';
      layers[MG.cur].style.opacity = '0';
      MG.cur = 1 - MG.cur;
      var cnt = el('mCount'); if(cnt) cnt.textContent = (target + 1) + ' / ' + n;
      var thumbs = el('mThumbs');
      if(thumbs){ var a = thumbs.querySelector('.th.active'); if(a) a.classList.remove('active');
        var t = thumbs.querySelector('.th[data-i="' + target + '"]'); if(t) t.classList.add('active'); }
      
      mgStop();
      if(vid && MG.urls.length > 1) {
        vid.onended = function() { mgGo(MG.i + 1); };
      } else if (MG.urls.length > 1) {
        MG.timer = setInterval(function(){ mgGo(MG.i + 1); }, 3200);
      }
    }
    function mgTimer(){ 
      mgStop();
      // Only set generic timer if current layer is NOT a video
      var curUrl = MG.urls[MG.i];
      if (curUrl && (curUrl.toLowerCase().endsWith('.mp4') || curUrl.toLowerCase().endsWith('.webm'))) {
        // Let the video onended handler take care of it
      } else if(MG.urls.length > 1) {
        MG.timer = setInterval(function(){ mgGo(MG.i + 1); }, 3200);
      }
    }
    function mgStop(){ clearInterval(MG.timer); MG.timer = null; }
    function mgStart(urls){
      mgStop(); MG.urls = urls || []; MG.i = 0; MG.cur = 0;
      var layers = mgLayers();
      var vid = setLayer(layers[0], urls[0]);
      layers[0].style.opacity = '1';
      setLayer(layers[1], '');
      layers[1].style.opacity = '0';
      urls.forEach(function(u){ 
        if(!u.toLowerCase().endsWith('.mp4') && !u.toLowerCase().endsWith('.webm')){
          var im = new Image(); im.src = u; 
        }
      });
      var multi = urls.length > 1;
      el('mPrev').style.display = multi ? '' : 'none';
      el('mNext').style.display = multi ? '' : 'none';
      el('mCount').style.display = multi ? '' : 'none';
      el('mCount').textContent = '1 / ' + urls.length;
      var thumbs = el('mThumbs');
      thumbs.innerHTML = multi
        ? urls.map(function(u, i){ 
            if(u.toLowerCase().endsWith('.mp4') || u.toLowerCase().endsWith('.webm')){
              return '<div class="th' + (i === 0 ? ' active' : '') + '" data-i="' + i + '" style="background-color:#000; position:relative;"><div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; color:#fff; font-size:10px;">▶</div></div>';
            }
            return '<div class="th' + (i === 0 ? ' active' : '') + '" data-i="' + i + '" style="background-image:url(\\'' + esc(u) + '\\')"></div>'; 
          }).join('')
        : '';
      Array.prototype.forEach.call(thumbs.querySelectorAll('.th'), function(th){
        th.addEventListener('click', function(){ mgGo(+th.getAttribute('data-i')); mgTimer(); });
      });
      
      if(vid && multi) {
        vid.onended = function() { mgGo(MG.i + 1); };
      } else if(multi) {
        mgTimer();
      }
    }'''

def patch_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = 'function mgLayers()'
    # The end string in the CURRENT file ends with "mgTimer();\n    }" inside mgStart
    # I need to match everything up to the end of mgStart.
    # We can use regex to find the block to replace.
    pattern = r'function mgLayers\(\)\{ return \[document\.querySelector\(\'\#mMain \.rm-base\'\).*?mgTimer\(\);\s*\}'
    
    match = re.search(pattern, content, re.DOTALL)
    if match:
        content = content[:match.start()] + new_mg_code + content[match.end():]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        print(f'Patched {filepath}')
    else:
        print(f'Could not find mgLayers block in {filepath}')

base_dir = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main'
for file in ['index.html', 'guest.html', 'book-packages.html', 'weddings.html']:
    fp = os.path.join(base_dir, file)
    patch_file(fp)
