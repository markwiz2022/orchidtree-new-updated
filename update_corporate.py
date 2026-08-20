import os

new_section = '''
  <!-- VIDEO HIGHLIGHTS -->
  <section class="features" style="background:var(--card); padding-top: 40px;">
    <div class="wrap">
      <div class="sec-head reveal">
        <div class="eyebrow">Real moments</div>
        <h2>Teams in action</h2>
        <p class="muted">Glimpses of recent corporate retreats and offsites at Orchid Tree.</p>
      </div>
      <div class="feature-grid reveal" style="grid-template-columns: repeat(3, 1fr);">
        <article class="fcard">
          <div class="fmedia" style="height: 350px;">
            <video src="images/uploads/corp_vid_cisco.mp4" autoplay muted loop playsinline style="width:100%; height:100%; object-fit:cover;"></video>
          </div>
          <div class="fbody" style="padding: 16px;">
            <h3>Cisco</h3>
          </div>
        </article>
        <article class="fcard">
          <div class="fmedia" style="height: 350px;">
            <video src="images/uploads/corp_vid_sap.mp4" autoplay muted loop playsinline style="width:100%; height:100%; object-fit:cover;"></video>
          </div>
          <div class="fbody" style="padding: 16px;">
            <h3>SAP Labs</h3>
          </div>
        </article>
        <article class="fcard">
          <div class="fmedia" style="height: 350px;">
            <video src="images/uploads/corp_vid_sagar.mp4" autoplay muted loop playsinline style="width:100%; height:100%; object-fit:cover;"></video>
          </div>
          <div class="fbody" style="padding: 16px;">
            <h3>Sagar Partners</h3>
          </div>
        </article>
      </div>
    </div>
  </section>
'''

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\corporate.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

idx = content.find('<!-- WORKSPACES')
if idx != -1:
    content = content[:idx] + new_section + content[idx:]
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Updated corporate.html')
else:
    print('Could not find WORKSPACES section')
