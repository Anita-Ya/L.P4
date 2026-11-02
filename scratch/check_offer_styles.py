with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
idx = css.find('.offer-cta-section')
print(css[idx:idx+2500])

