with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
idx1 = css.find('.offer-cta-section')
idx2 = css.find('.faq-section')

section9_css = css[idx1:idx2]
colors = set(re.findall(r'#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)', section9_css))
print("Colors in Section 9:")
for c in sorted(colors):
    print(c)

