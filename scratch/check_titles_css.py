with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
titles = ['product-main-title', 'quality-title', 'reviews-main-title', 'ingredients-title']
for t in titles:
    pattern = rf'\.{t}\s*\{{[^}}]*\}}'
    m = re.search(pattern, css)
    if m:
        print(f"=== {t} ===")
        print(m.group(0))

