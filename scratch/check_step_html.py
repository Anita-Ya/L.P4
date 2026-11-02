import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

idx = html.find('assets/step1-public-fear.jpg')
print(html[idx-200:idx+200])
