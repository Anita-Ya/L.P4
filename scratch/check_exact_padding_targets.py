import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

targets = [
    ('.problem-detailing-section.light-theme', r'padding:\s*38px\s*14px\s*44px\s*14px;'),
    ('.product-intro-section', r'padding:\s*34px\s*14px\s*34px\s*14px;'),
    ('.features-section', r'padding:\s*34px\s*14px\s*34px\s*14px;'),
    ('.ingredients-section', r'padding:\s*34px\s*14px\s*44px\s*14px;'),
    ('.quality-trust-section', r'padding:\s*44px\s*18px\s*50px\s*18px;'),
    ('.customer-reviews-section', r'padding:\s*42px\s*16px\s*54px\s*16px;'),
    ('.doctor-rec-section', r'padding:\s*42px\s*16px\s*52px\s*16px;'),
    ('.offer-cta-section', r'padding:\s*30px\s*16px\s*56px\s*16px;'),
    ('.faq-section', r'padding:\s*42px\s*16px\s*54px\s*16px;')
]

for name, pattern in targets:
    m = re.search(pattern, css)
    print(f"{name}: {'FOUND' if m else 'NOT FOUND'}")

