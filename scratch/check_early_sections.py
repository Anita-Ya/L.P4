import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's inspect root colors and section backgrounds for sections 1-6
sections = [
    'hero-banner',
    'problem-section',
    'split-product-stage',
    'features-section',
    'ingredients-section',
    'quality-trust-section'
]

for sec in sections:
    idx = css.find(f'.{sec}')
    print(f"\n=== {sec} (idx: {idx}) ===")
    if idx != -1:
        # print first 400 chars of this section
        print(css[idx:idx+350])

