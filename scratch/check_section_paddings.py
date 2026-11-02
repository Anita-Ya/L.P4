with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

section_classes = [
    'hero-banner',
    'problem-detailing-section',
    'split-product-stage',
    'split-intro-block',
    'features-section',
    'ingredients-section',
    'quality-trust-section',
    'reviews-section',
    'doctor-rec-section',
    'offer-cta-section',
    'faq-section',
    'order-form-section'
]

for sc in section_classes:
    pattern = rf'\.{sc}[^{{\n]*\{{[^}}]*\}}'
    matches = re.findall(pattern, css)
    print(f"=== {sc} ===")
    for m in matches[:2]:
        # print padding and margin lines
        for line in m.splitlines():
            if 'padding' in line or 'margin' in line:
                print(f"  {line.strip()}")

