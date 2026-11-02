with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
idx = css.find('Special Offer Ticket Coupon Box')
print(css[idx:idx+1500])

