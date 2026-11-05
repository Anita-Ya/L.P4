import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
for m in re.finditer(r'(\.faq-section|\.order-form-section)\s*\{[^}]*\}', css):
    print(m.group(0))
