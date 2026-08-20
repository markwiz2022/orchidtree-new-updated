import os

filepath = r'C:\Users\ASUS\.gemini\antigravity\scratch\orchid-tree-website-main (1)\orchid-tree-website-main\guest.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()
    
start = content.find('function mgStart(urls){')
end = content.find('</script>', start)
print(content[start:start+1000])
