import re, sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

for m in re.finditer(r'<img[^>]*src=[\'"]([^\'"]*step[^\'"]*)[\'"][^>]*>', html):
    print(m.group(0))
