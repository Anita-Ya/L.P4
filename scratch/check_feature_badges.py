with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
idx = css.find('.offer-feature-icon-badge')
print(css[idx-200:idx+800])

