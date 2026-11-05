import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
matches = re.findall(r'([.#][\w-]+\s*\{[^}]*(?:ayur-trust|order-trust|ayur-order-card|order-form-section|faq-section)[^}]*\})', css)
for m in matches:
    print(m)
    print("="*40)
