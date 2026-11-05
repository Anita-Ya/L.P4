import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/main.js', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'function scrollToOrder[^{]*\{[^}]*\}', text)
if m:
    print(m.group(0))

