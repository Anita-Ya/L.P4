with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
idx1 = css.find('.doctor-rec-section')
idx2 = css.find('.offer-cta-section')

section8_css = css[idx1:idx2]
colors = set(re.findall(r'#[0-9a-fA-F]{3,8}|rgba?\([^)]+\)', section8_css))
print("Colors in Section 8:")
for c in sorted(colors):
    print(c)

