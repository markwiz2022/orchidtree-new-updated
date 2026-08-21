import re
with open("index.html", "r", encoding="utf-8") as f: content = f.read()
repl = """<div class="eyebrow">What's included</div>
          <h2>Everything you need, nothing you don't</h2>
          <p class="muted" style="margin-bottom:28px;">Your room charge includes all meals prepared to your preference, full access to the estate, and one full-body massage, while accompanying guests enjoy a traditional Kansa foot massage.</p>
          <div class="incl-cols" style="margin-top:28px;">"""
search = """<div class="eyebrow">What's included</div>
          <h2>Everything you need, nothing you don't</h2>
          <div class="incl-cols" style="margin-top:28px;">"""
content = content.replace(search, repl)
with open("index.html", "w", encoding="utf-8") as f: f.write(content)
print("done")
