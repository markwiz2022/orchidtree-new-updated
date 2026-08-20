import os

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
      var cnt = document.getElementById('mCount') || el('mCount'); if(cnt) cnt.textContent = (target + 1) + ' / ' + n;
      var thumbs = document.getElementById('mThumbs') || el('mThumbs');
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
      var curUrl = MG.urls[MG.i];
      if (curUrl && (curUrl.toLowerCase().endsWith('.mp4') || curUrl.toLowerCase().endsWith('.webm'))) {
        // video handles its own advancement
      } else if(MG.urls.length > 1) {
        MG.timer = setInterval(function(){ mgGo(MG.i + 1); }, 3200);
      }
    }
    function mgStop(){ clearInterval(MG.timer); MG.timer = null; }
    function mgStart(urls){
      mgStop(); MG.urls = urls || []; MG.i = 0; MG.cur = 0;
      var layers = mgLayers();
      var vid = setLayer(layers[0], MG.urls[0]);
      layers[0].style.opacity = '1';
      setLayer(layers[1], '');
      layers[1].style.opacity = '0';
      MG.urls.forEach(function(u){ 
        if(u && !u.toLowerCase().endsWith('.mp4') && !u.toLowerCase().endsWith('.webm')){
          var im = new Image(); im.src = u; 
        }
      });
      var multi = MG.urls.length > 1;
      
      var _elPrev = document.getElementById('mPrev') || (typeof el !== 'undefined' ? el('mPrev') : null);
      var _elNext = document.getElementById('mNext') || (typeof el !== 'undefined' ? el('mNext') : null);
      var _elCount = document.getElementById('mCount') || (typeof el !== 'undefined' ? el('mCount') : null);
      var _elThumbs = document.getElementById('mThumbs') || (typeof el !== 'undefined' ? el('mThumbs') : null);
      
      if(_elPrev) _elPrev.style.display = multi ? '' : 'none';
      if(_elNext) _elNext.style.display = multi ? '' : 'none';
      if(_elCount) {
        _elCount.style.display = multi ? '' : 'none';
        _elCount.textContent = '1 / ' + MG.urls.length;
      }
      
      if(_elThumbs) {
          _elThumbs.innerHTML = multi
            ? MG.urls.map(function(u, i){ 
                if(u && (u.toLowerCase().endsWith('.mp4') || u.toLowerCase().endsWith('.webm'))){
                  return '<div class="th' + (i === 0 ? ' active' : '') + '" data-i="' + i + '" style="background-color:#000; position:relative;"><div style="position:absolute; inset:0; display:flex; align-items:center; justify-content:center; color:#fff; font-size:10px;">▶</div></div>';
                }
                return '<div class="th' + (i === 0 ? ' active' : '') + '" data-i="' + i + '" style="background-image:url(\\'' + esc(u) + '\\')"></div>'; 
              }).join('')
            : '';
          Array.prototype.forEach.call(_elThumbs.querySelectorAll('.th'), function(th){
            th.addEventListener('click', function(){ mgGo(+th.getAttribute('data-i')); mgTimer(); });
          });
      }
      
      if(vid && multi) {
        vid.onended = function() { mgGo(MG.i + 1); };
      } else if(multi) {
        mgTimer();
      }
    }
    '''

def patch_file(filepath):
    if not os.path.exists(filepath): return
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    start_str = 'function mgLayers(){ return [document.querySelector'
    
    # We find the end by searching for the end of mgStart() which has `mgTimer();\n    }`
    import re
    match = re.search(r'function mgLayers\(\)\{.*?mgTimer\(\);\s*\}\s*(?:\r?\n)+\s*(el|document\.getElementById)\(\'mPrev\'\)\.addEventListener\(', content, re.DOTALL)
    
    if match:
        end_idx = match.end() - len(match.group(1) + "('mPrev').addEventListener(")
        new_content = content[:match.start()] + new_mg_code + '\n    ' + content[end_idx:]
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f'Patched {filepath}')
    else:
        print(f'Could not find block in {filepath}')

base_dir = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main'
for file in ['index.html', 'guest.html', 'book-packages.html']:
    fp = os.path.join(base_dir, file)
    patch_file(fp)
