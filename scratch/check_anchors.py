import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'href=[\'"][^\'"]*[\'"]|onclick=[\'"][^\'"]*[\'"]', text)
for m in matches:
    if 'order' in m.lower() or 'faq' in m.lower():
        print(m)

