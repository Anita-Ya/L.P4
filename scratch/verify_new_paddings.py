import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

targets = [
    'problem-detailing-section',
    'product-intro-section',
    'features-section',
    'ingredients-section',
    'quality-trust-section',
    'customer-reviews-section',
    'doctor-rec-section',
    'offer-cta-section',
    'faq-section'
]

for name in targets:
    m = re.search(rf'\.{name}[^{{\n]*\{{[^}}]*\}}', css)
    if m:
        for line in m.group(0).splitlines():
            if 'padding' in line:
                print(f"{name}: {line.strip()}")

