with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
for cls in ['.product-intro-section', '.product-header', '.problem-detailing-section', '.features-section', '.ingredients-section', '.quality-trust-section', '.customer-reviews-section', '.reviews-section']:
    idx = css.find(cls)
    if idx != -1:
        print(f"=== {cls} ===")
        print(css[idx:idx+350])

