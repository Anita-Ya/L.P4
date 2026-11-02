with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

header_classes = ['problem-header', 'product-header', 'features-top-bar', 'ingredients-header', 'quality-header', 'reviews-header', 'faq-header']

for hc in header_classes:
    pattern = rf'\.{hc}\s*\{{[^}}]*\}}'
    m = re.search(pattern, css)
    if m:
        print(f"=== {hc} ===")
        print(m.group(0))

