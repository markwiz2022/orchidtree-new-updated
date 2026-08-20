
  (function(){
    var C = window.OrchidCatalog, CT = window.OrchidContent;
    function esc(s){ return String(s==null?'':s).replace(/&/g,'&amp;').replace(/</g,'&lt;').replace(/>/g,'&gt;'); }
    function stars(n){ var f=Math.round(n),s=''; for(var i=0;i<5;i++) s+= i<f?'★':'☆'; return s; }

    // ---- hero video: skip the logo intro at the start, loop from there ----
    var HERO_START = 4; // seconds to skip (adjust if the logo is shorter/longer)
    var hv = document.getElementById('heroVideo');
    if(hv){
      var toStart = function(){ try{ hv.currentTime = HERO_START; }catch(e){} };
      hv.addEventListener('loadedmetadata', toStart);
      if(hv.readyState >= 1) toStart();
      hv.addEventListener('seeked', function(){ hv.classList.add('ready'); });
      var loopBack = function(){ try{ hv.currentTime = HERO_START; hv.play(); }catch(e){} };
      hv.addEventListener('ended', loopBack);
      hv.addEventListener('timeupdate', function(){ if(hv.duration && hv.currentTime > hv.duration - 0.3) loopBack(); });
    }

    // ---- nav solidify on scroll ----
    var nav = document.getElementById('nav');
    function navScroll(){ if(window.scrollY > 60) nav.classList.add('solid'); else nav.classList.remove('solid'); }
    window.addEventListener('scroll', navScroll, {passive:true}); navScroll();

    // ---- compact Reserve pill: appears once you scroll past the hero ----
    var fab = document.getElementById('bookFab');
    function toggleFab(){ if(fab){ if(window.scrollY > window.innerHeight * 0.85) fab.classList.add('show'); else fab.classList.remove('show'); } }
    window.addEventListener('scroll', toggleFab, {passive:true}); toggleFab();

    // ---- scroll reveal ----
    var io = new IntersectionObserver(function(entries){
      entries.forEach(function(e){ if(e.isIntersecting){ e.target.classList.add('in'); io.unobserve(e.target); } });
    }, {threshold:0.14});
    document.querySelectorAll('.reveal').forEach(function(el){ io.observe(el); });

    // ---- FAQ accordion ----
    document.querySelectorAll('.faq-q').forEach(function(q){
      q.addEventListener('click', function(){ var it=q.parentElement;var wasOpen=it.classList.contains('open');it.parentElement.querySelectorAll('.faq-item.open').forEach(function(o){o.classList.remove('open');});if(!wasOpen)it.classList.add('open'); });
    });

    // ---- self-serve book bar: dates + guests dropdowns ----
    (function(){
      var datesTrigger = document.getElementById('bbDatesTrigger');
      var datesPop     = document.getElementById('bbDatesPop');
      var datesField   = document.getElementById('bbDatesField');
      var datesValue   = document.getElementById('bbDatesValue');
      var arriveEl = document.getElementById('bbArrive');
      var leaveEl  = document.getElementById('bbLeave');
      var guestsTrigger = document.getElementById('bbGuestsTrigger');
      var guestPop      = document.getElementById('bbGuestPop');
      var guestsField   = document.getElementById('bbGuestsField');
      var summary       = document.getElementById('bbGuestSummary');
      var checkBtn = document.getElementById('checkAvail');
      if(!arriveEl || !leaveEl || !guestPop || !checkBtn) return;

      function fmt(d){
        var y=d.getFullYear(), m=('0'+(d.getMonth()+1)).slice(-2), day=('0'+d.getDate()).slice(-2);
        return y+'-'+m+'-'+day;
      }
      function addDays(d,n){ var x=new Date(d); x.setDate(x.getDate()+n); return x; }
      var MON=['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'];
      function pretty(iso){ if(!iso) return null; var p=iso.split('-'); return parseInt(p[2],10)+' '+MON[parseInt(p[1],10)-1]; }

      // defaults: arrive today, leave tomorrow
      var today = new Date(); today.setHours(0,0,0,0);
      var tomorrow = addDays(today,1);
      arriveEl.value = fmt(today);   arriveEl.min = fmt(today);
      leaveEl.value  = fmt(tomorrow); leaveEl.min = fmt(tomorrow);

      // pre-fill from URL params (lossless return from "Edit" on the options page)
      var qp = new URLSearchParams(location.search);
      if(qp.get('in'))  arriveEl.value = qp.get('in');
      if(qp.get('out')) leaveEl.value  = qp.get('out');

      function updateDatesValue(){
        var a=pretty(arriveEl.value), b=pretty(leaveEl.value);
        datesValue.textContent = (a && b) ? (a+' – '+b) : 'Add your dates';
      }
      arriveEl.addEventListener('change', function(){
        var a = arriveEl.value ? new Date(arriveEl.value) : today;
        leaveEl.min = fmt(addDays(a,1));
        if(!leaveEl.value || new Date(leaveEl.value) <= a){ leaveEl.value = fmt(addDays(a,1)); }
        updateDatesValue();
      });
      leaveEl.addEventListener('change', updateDatesValue);
      updateDatesValue();

      // clicking anywhere in a date cell opens that native picker
      Array.prototype.forEach.call(datesPop.querySelectorAll('.bb-date-cell'), function(cell){
        cell.addEventListener('click', function(ev){
          var inp = cell.querySelector('input');
          if(inp && inp.showPicker && ev.target !== inp){ try{ inp.showPicker(); }catch(e){} }
        });
      });

      // ---- guests stepper ----
      var counts = { adults:2, children:0, pets:0 };
      var mins   = { adults:1, children:0, pets:0 };
      ['adults','children','pets'].forEach(function(k){
        var v = parseInt(qp.get(k),10);
        if(isFinite(v) && v >= mins[k]) counts[k] = v;
      });
      function plural(n,word){ return n+' '+word+(n===1?'':'s'); }
      function updateSummary(){
        var parts = [plural(counts.adults,'adult')];
        parts.push(counts.children + ' ' + (counts.children===1?'child':'children')); // always shown
        if(counts.pets>0) parts.push(plural(counts.pets,'pet'));
        summary.textContent = parts.join(' · ');
      }
      function refreshSteppers(){
        guestPop.querySelectorAll('.bb-step').forEach(function(btn){
          var key = btn.getAttribute('data-step'), dir = parseInt(btn.getAttribute('data-dir'),10);
          if(dir < 0) btn.disabled = counts[key] <= mins[key];
        });
        document.getElementById('bbAdults').textContent = counts.adults;
        document.getElementById('bbChildren').textContent = counts.children;
        document.getElementById('bbPets').textContent = counts.pets;
      }
      guestPop.querySelectorAll('.bb-step').forEach(function(btn){
        btn.addEventListener('click', function(ev){
          ev.stopPropagation();
          var key = btn.getAttribute('data-step'), dir = parseInt(btn.getAttribute('data-dir'),10);
          var next = counts[key] + dir;
          if(next < mins[key]) next = mins[key];
          counts[key] = next;
          refreshSteppers(); updateSummary();
        });
      });
      updateSummary(); refreshSteppers();

      // ---- dropdown manager: one open at a time, click-out / Esc to close ----
      var POPS = [
        { t:datesTrigger,  p:datesPop,  f:datesField },
        { t:guestsTrigger, p:guestPop,  f:guestsField },
      ];
      function closeAll(except){
        POPS.forEach(function(o){
          if(o.p !== except){ o.p.hidden = true; o.p.classList.remove('bb-pop--up'); o.t.setAttribute('aria-expanded','false'); }
        });
      }
      // open above the bar when there isn't enough room below
      function placePop(o){
        o.p.classList.remove('bb-pop--up');
        var tr = o.t.getBoundingClientRect();
        var popH = o.p.offsetHeight;
        var below = window.innerHeight - tr.bottom;
        var above = tr.top;
        if(below < popH + 24 && above > below) o.p.classList.add('bb-pop--up');
      }
      POPS.forEach(function(o){
        o.t.addEventListener('click', function(ev){
          ev.stopPropagation();
          var willOpen = o.p.hidden;
          closeAll(willOpen ? o.p : null);
          o.p.hidden = !willOpen;
          o.t.setAttribute('aria-expanded', String(willOpen));
          if(willOpen) placePop(o);
        });
        o.t.addEventListener('keydown', function(ev){
          if(ev.key==='Enter' || ev.key===' '){ ev.preventDefault(); o.t.click(); }
        });
        o.p.addEventListener('click', function(ev){ ev.stopPropagation(); });
      });
      document.addEventListener('click', function(ev){
        var inside = POPS.some(function(o){ return o.f.contains(ev.target); });
        if(!inside) closeAll(null);
      });
      document.addEventListener('keydown', function(ev){ if(ev.key==='Escape') closeAll(null); });

      // ---- check availability → straight to the package options ----
      checkBtn.addEventListener('click', function(){
        window.location.href = 'book-packages.html?in=' + encodeURIComponent(arriveEl.value) +
          '&out=' + encodeURIComponent(leaveEl.value) +
          '&adults=' + encodeURIComponent(counts.adults) +
          '&children=' + encodeURIComponent(counts.children) +
          '&pets=' + encodeURIComponent(counts.pets);
      });
    })();

    // ---- anchors: smooth scroll ----
    document.querySelectorAll('a[href^="#"]').forEach(function(a){
      a.addEventListener('click', function(ev){ var t=document.querySelector(a.getAttribute('href')); if(t){ ev.preventDefault(); t.scrollIntoView({behavior:'smooth'}); } });
    });

    // ---- EXPERIENCES shorts (built from real photos) ----
    var U = 'https://orchidtree.in/uploads/';
    var SHORTS = [
      { lbl:'Ozone pool',                 img:'images/ozone-pool.jpg' },
      { lbl:'Farm visit',                 img:'images/uploads/farm_0K1A1757.JPG' },
      { lbl:'Bonfire & stargazing',       img:'images/uploads/bonfire.jpg' },
      { lbl:'Steam & open-sky showers',   img:'images/uploads/steam.jpg' },
      { lbl:'Karaoke & music corner',     img:'images/uploads/karaoke_0K1A7846.JPG' },
      { lbl:'Trampoline & games',         img:'images/uploads/trampoline_0K1A9822.JPG' },
      { lbl:'Birdwatching & trails',      img:'images/uploads/forest_Test-8274806.jpg' },
      { lbl:'Movies in the hall',         img:'images/uploads/movie.jpg' },
      { lbl:'Carrom',                     img:'images/uploads/chess_0K1A9971.JPG' },
      { lbl:'Kansa',                      img:'images/uploads/kansa.jpg' },
      { lbl:'Billiards',                  img:'images/uploads/Pool_Table_74b3551af2.JPG' },
      { lbl:'Chess',                      img:'images/uploads/chess_0K1A9971.JPG' }
    ];
    document.getElementById('expShorts').innerHTML = SHORTS.map(function(s){
      return '<div class="short"><div class="ph" style="background-image:url(\''+esc(s.img)+'\')"></div><div class="scrim"></div><div class="lbl">'+esc(s.lbl)+'</div></div>';
    }).join('');
    (function(){
      var sh=document.getElementById('expShorts'), nav=document.getElementById('expNav'), fade=document.getElementById('expFade');
      var prev=document.getElementById('expPrev'), next=document.getElementById('expNext');
      function step(){ var t=sh.querySelector('.short'); return (t?t.getBoundingClientRect().width:260)+18; }
      function sync(){
        var over=sh.scrollWidth-sh.clientWidth>4;
        nav.style.visibility=over?'visible':'hidden';
        fade.style.opacity=(over && sh.scrollLeft < sh.scrollWidth-sh.clientWidth-4)?'1':'0';
        prev.disabled=sh.scrollLeft<=2; next.disabled=sh.scrollLeft>=sh.scrollWidth-sh.clientWidth-2;
      }
      prev.onclick=function(){ sh.scrollBy({left:-step()*2,behavior:'smooth'}); };
      next.onclick=function(){ sh.scrollBy({left:step()*2,behavior:'smooth'}); };
      sh.addEventListener('scroll',sync,{passive:true}); window.addEventListener('resize',sync); sync();
    })();

    // ---- horizontal parallax: each image drifts L→R as you scroll the carousel ----
    (function(){
      if(window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches) return;
      var sh = document.getElementById('expShorts'); if(!sh) return;
      function parallax(){
        var rect = sh.getBoundingClientRect(), vw = rect.width || 1;
        Array.prototype.forEach.call(sh.querySelectorAll('.short'), function(card){
          var ph = card.querySelector('.ph'); if(!ph) return;
          var cr = card.getBoundingClientRect();
          var prog = ((cr.left + cr.width / 2) - rect.left) / vw;   // 0 at left edge, 1 at right
          prog = Math.max(0, Math.min(1, prog));
          var x = -prog * (card.clientWidth * 0.28);                // pan within the 32% of extra width
          ph.style.transform = 'translateX(' + x.toFixed(1) + 'px)';
        });
      }
      var ticking = false;
      function tick(){ if(!ticking){ ticking = true; requestAnimationFrame(function(){ parallax(); ticking = false; }); } }
      sh.addEventListener('scroll', tick, {passive:true});
      window.addEventListener('resize', tick);
      tick();
    })();

    // ---- ROOM cards: cover photo + crossfade through the gallery on hover ----
    document.querySelectorAll('.room[data-rep]').forEach(function(card){
      var r = C && C.get(card.getAttribute('data-rep')); if(!r) return;
      // clicking the card opens the rich room-detail modal for that room
      card.style.cursor = 'pointer';
      card.addEventListener('click', function(){ if(window.openRoom) window.openRoom(card.getAttribute('data-rep')); });
      var urls = (r.imageUrls||[]).slice();
      var base = card.querySelector('.rmh-base'), top = card.querySelector('.rmh-top');
      if(urls[0]) base.style.backgroundImage = "url('"+urls[0]+"')";
      // photo count badge
      if(urls.length>1){ var b=document.createElement('div'); b.className='rcount'; b.textContent=urls.length+' photos'; card.querySelector('.media').appendChild(b); }
      if(urls.length<2) return;
      var cur=0, idx=0, loaded=false;
      function preload(){ if(loaded) return; loaded=true; urls.forEach(function(u){ var im=new Image(); im.src=u; }); }
      function tick(){
        if(!card._hover) return;
        idx=(idx+1)%urls.length;
        var layers=[base,top], incoming=layers[1-cur];
        incoming.style.backgroundImage="url('"+urls[idx]+"')";
        incoming.style.opacity='1'; layers[cur].style.opacity='0'; cur=1-cur;
        card._t=setTimeout(tick,2200);
      }
      card.addEventListener('mouseenter',function(){ card._hover=true; preload(); card._t=setTimeout(tick,500); });
      card.addEventListener('mouseleave',function(){
        card._hover=false; clearTimeout(card._t);
        base.style.backgroundImage="url('"+urls[0]+"')"; base.style.opacity='1'; top.style.opacity='0'; cur=0; idx=0;
      });
    });

    // ---- REVIEWS from content.js (kept in sync with the guest page) ----
    if(CT && CT.reviews){
      var ids = ['aditi','ketty','srikant'];
      var picked = ids.map(function(id){ return CT.getReview(id); }).filter(Boolean);
      document.getElementById('revGrid').innerHTML = picked.map(function(r){
        return '<div class="rev"><div class="stars">'+stars(r.rating)+'</div><p>"'+esc(r.text)+'"</p>'+
          '<div class="who">'+esc(r.name)+'</div><div class="vg">'+(r.verified?'Verified Guest':'')+'</div></div>';
      }).join('');
      var url = CT.googleReviewsUrl;
      document.getElementById('revFoot').innerHTML = '<b>4.4</b> from '+(url?'<a href="'+esc(url)+'" target="_blank" rel="noopener">615+ Google reviews</a>':'615+ Google reviews');
    }

    // ============================================================
    //  RICH ROOM MODAL (ported from book-packages.html / guest.html)
    // ============================================================
    function el(id){ return document.getElementById(id); }

    // ---- zone: poolside cluster vs garden cottage (the estate's two areas) -
    var ICON_POOL = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M2 16c1.5 0 1.5 1.2 3 1.2S8.5 16 10 16s1.5 1.2 3 1.2 1.5-1.2 3-1.2 1.5 1.2 3 1.2"/><path d="M2 20c1.5 0 1.5 1.2 3 1.2S8.5 20 10 20s1.5 1.2 3 1.2 1.5-1.2 3-1.2 1.5 1.2 3 1.2"/><path d="M7 16V5.5A1.5 1.5 0 0 1 8.5 4 1.5 1.5 0 0 1 10 5.5"/><path d="M16 16V5.5A1.5 1.5 0 0 0 14.5 4 1.5 1.5 0 0 0 13 5.5"/></svg>';
    var ICON_GARDEN = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"><path d="M12 22v-7"/><path d="M12 15c-3.5 0-6-2.4-6-5.8C6 5.6 8.7 3 12 3s6 2.6 6 6.2c0 3.4-2.5 5.8-6 5.8z"/><path d="M12 15c0-2.5 1.3-4.5 3-5.5M12 12c0-2-1-3.6-2.5-4.4"/></svg>';
    function zoneOf(category){ return /garden/i.test(category||'') ? 'garden' : 'pool'; }
    function zoneLabel(category){ return zoneOf(category) === 'garden' ? 'Garden cottage' : 'Poolside'; }
    function zoneTag(category){
      var z = zoneOf(category);
      var ic = z === 'garden' ? ICON_GARDEN : ICON_POOL;
      return '<span class="zone '+z+'">'+ic+zoneLabel(category)+'</span>';
    }
    var SETTING_COPY = {
      pool: { title: 'By the pool', text: 'Steps from the water and clustered together with the other poolside rooms. Bright, easy and close to everything — the natural choice when your group wants to stay near each other and the pool.' },
      garden: { title: 'A garden cottage, set apart', text: 'Tucked among the trees a short walk from the pool, with a private sit-out patio and a bath open to the sky. Quieter and more private — its own little world, a little removed from the poolside rooms.' },
    };
    function settingBand(category){
      var z = zoneOf(category), c = SETTING_COPY[z], ic = z === 'garden' ? ICON_GARDEN : ICON_POOL;
      return '<div class="setting-band '+z+'"><div class="sb-ic">'+ic+'</div>'+
        '<div><div class="sb-title">'+esc(c.title)+'</div><div class="sb-text">'+esc(c.text)+'</div></div></div>';
    }

    function rupees(n){ return '₹' + Number(n||0).toLocaleString('en-IN'); }
    var WA_NUM = (CT && CT.contact && CT.contact.whatsapp) || '918088251913';
    function waLink(msg){ return 'https://wa.me/' + WA_NUM + '?text=' + encodeURIComponent(msg); }

    // ---- gallery (crossfade + thumbs + autoplay) ----
    function roomUrls(r){ return (r.imageUrls && r.imageUrls.length) ? r.imageUrls : (r.imageUrl ? [r.imageUrl] : []); }
    var MG = { urls: [], i: 0, cur: 0, timer: null };
    function mgLayers(){ return [document.querySelector('#mMain .rm-base'), document.querySelector('#mMain .rm-top')]; }
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
            return '<div class="th' + (i === 0 ? ' active' : '') + '" data-i="' + i + '" style="background-image:url(\'' + esc(u) + '\')"></div>'; 
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
    });
      });
      mgTimer();
    }
    el('mPrev').addEventListener('click', function(){ mgGo(MG.i - 1); mgTimer(); });
    el('mNext').addEventListener('click', function(){ mgGo(MG.i + 1); mgTimer(); });

    // ---- requirement collector (dates + guests → book-packages for THIS room) ----
    var currentRoomId = null;
    (function(){
      var ctaBox  = el('rbookCta'), collect = el('rbookCollect');
      var openBtn = el('rbookOpen'), submit = el('rcSubmit');
      var arr = el('rcArrive'), lv = el('rcLeave');
      var counts = { adults: 2, children: 0, pets: 0 };
      var mins   = { adults: 1, children: 0, pets: 0 };

      function fmt(d){ var y=d.getFullYear(),m=('0'+(d.getMonth()+1)).slice(-2),day=('0'+d.getDate()).slice(-2); return y+'-'+m+'-'+day; }
      function addDays(d,n){ var x=new Date(d); x.setDate(x.getDate()+n); return x; }

      function refresh(){
        collect.querySelectorAll('.bb-step').forEach(function(b){
          var k=b.getAttribute('data-rc'), d=parseInt(b.getAttribute('data-dir'),10);
          if(d<0) b.disabled = counts[k] <= mins[k];
        });
        el('rcAdults').textContent = counts.adults;
        el('rcChildren').textContent = counts.children;
        el('rcPets').textContent = counts.pets;
      }
      collect.querySelectorAll('.bb-step').forEach(function(b){
        b.addEventListener('click', function(){
          var k=b.getAttribute('data-rc'), d=parseInt(b.getAttribute('data-dir'),10);
          var n=counts[k]+d; if(n<mins[k]) n=mins[k]; counts[k]=n; refresh();
        });
      });

      // clicking a date cell opens that native picker
      Array.prototype.forEach.call(collect.querySelectorAll('.rc-date'), function(cell){
        cell.addEventListener('click', function(ev){
          var inp = cell.querySelector('input');
          if(inp && inp.showPicker && ev.target !== inp){ try{ inp.showPicker(); }catch(e){} }
        });
      });
      arr.addEventListener('change', function(){
        var today=new Date(); today.setHours(0,0,0,0);
        var a = arr.value ? new Date(arr.value) : today;
        lv.min = fmt(addDays(a,1));
        if(!lv.value || new Date(lv.value) <= a) lv.value = fmt(addDays(a,1));
      });

      // reset to State A with fresh defaults — called each time a room opens
      window._rbookReset = function(){
        var today=new Date(); today.setHours(0,0,0,0);
        arr.value = fmt(today);   arr.min = fmt(today);
        lv.value  = fmt(addDays(today,1)); lv.min = fmt(addDays(today,1));
        counts = { adults: 2, children: 0, pets: 0 };
        refresh();
        collect.classList.remove('open');
        ctaBox.hidden = false;
      };

      openBtn.addEventListener('click', function(){
        ctaBox.hidden = true;
        collect.classList.add('open');
      });

      submit.addEventListener('click', function(){
        if(!arr.value || !lv.value || new Date(lv.value) <= new Date(arr.value)){
          lv.focus(); return;
        }
        if(!currentRoomId) return;
        var u = new URLSearchParams();
        u.set('room', currentRoomId);
        u.set('in', arr.value);
        u.set('out', lv.value);
        u.set('adults', String(counts.adults));
        u.set('children', String(counts.children));
        u.set('pets', String(counts.pets));
        window.location.href = 'book-packages.html?' + u.toString();
      });
    })();

    function openRoom(id){
      var r = C && C.get(id); if(!r) return;
      currentRoomId = id;
      el('mCat').textContent = r.category;
      el('mTitle').textContent = r.name;
      el('mTagline').innerHTML = esc(r.tagline) + (r.tier ? '<span class="tier">'+esc(r.tier)+'</span>' : '');
      el('mZone').innerHTML = zoneTag(r.category);
      el('mSetting').innerHTML = settingBand(r.category);
      el('mStory').textContent = r.story || '';
      el('mDesc').textContent = r.description || '';

      var priceEl = el('mPrice');
      if(r.priceFrom){ priceEl.style.display=''; priceEl.textContent = 'From ' + rupees(r.priceFrom) + ' + taxes per night.'; }
      else { priceEl.style.display='none'; }

      mgStart(roomUrls(r));

      el('mFacts').innerHTML = (r.facts || []).map(function(f){
        return '<div class="f"><span class="k">'+esc(f.label)+'</span><span class="v">'+esc(f.value)+'</span></div>';
      }).join('');
      el('mOffers').innerHTML = (r.amenities || []).map(function(a){ return '<span class="a">'+esc(a)+'</span>'; }).join('');
      el('mAsk').innerHTML = '<a class="room-ask" href="'+esc(waLink('Hi, I have a question about the '+r.name+' room at Orchid Tree.'))+'" target="_blank" rel="noopener">Have a question about this room? Message us &rarr;</a>';

      if(window._rbookReset) window._rbookReset();

      el('overlay').classList.add('open');
      document.body.style.overflow = 'hidden';
    }
    function closeRoom(){ mgStop(); el('overlay').classList.remove('open'); document.body.style.overflow = ''; }
    window.openRoom = openRoom;
    window.closeRoom = closeRoom;
    document.addEventListener('keydown', function(ev){ if(ev.key === 'Escape') closeRoom(); });
  })();
  