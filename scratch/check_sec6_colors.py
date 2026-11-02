with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
idx1 = css.find('.quality-trust-section')
idx2 = css.find('.reviews-section')

section6_css = css[idx1:idx2]
colors = set(re.findall(r'#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)', section6_css))
print("Colors in Section 6:")
for c in sorted(colors):
    print(c)

