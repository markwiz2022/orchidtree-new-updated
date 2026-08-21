import os

filepath = 'guest.html'
with open(filepath, 'r', encoding='utf-8') as f:
    html = f.read()

start_idx = html.find('function mgStart(urls){')
end_idx = html.find("el('mPrev').addEventListener(", start_idx)

mgStart_correct = """function mgStart(urls){
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
    }
    """

html = html[:start_idx] + mgStart_correct + html[end_idx:]

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(html)
print("Fixed guest.html")
