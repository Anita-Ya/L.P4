import re

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update Section 2 Problem Detailing padding
css = re.sub(
    r'(\.problem-detailing-section\.light-theme\s*\{[^}]*?)padding:\s*38px\s*14px\s*44px\s*14px;',
    r'\1padding: 24px 14px 16px 14px;',
    css
)

# 2. Update Section 3 Product Intro padding
css = re.sub(
    r'(\.product-intro-section\s*\{[^}]*?)padding:\s*34px\s*14px\s*34px\s*14px;',
    r'\1padding: 16px 14px 18px 14px;',
    css
)

# 3. Update Section 4 Features padding
css = re.sub(
    r'(\.features-section\s*\{[^}]*?)padding:\s*34px\s*14px\s*34px\s*14px;',
    r'\1padding: 16px 14px 18px 14px;',
    css
)

# 4. Update Section 5 Ingredients padding
css = re.sub(
    r'(\.ingredients-section\s*\{[^}]*?)padding:\s*34px\s*14px\s*44px\s*14px;',
    r'\1padding: 16px 14px 20px 14px;',
    css
)

# 5. Update Section 6 Quality Trust padding
css = re.sub(
    r'(\.quality-trust-section\s*\{[^}]*?)padding:\s*44px\s*18px\s*50px\s*18px;',
    r'\1padding: 18px 14px 20px 14px;',
    css
)

# 6. Update Section 7 Customer Reviews padding
css = re.sub(
    r'(\.customer-reviews-section\s*\{[^}]*?)padding:\s*42px\s*16px\s*54px\s*16px;',
    r'\1padding: 20px 14px 22px 14px;',
    css
)

# 7. Update Section 8 Doctor Recommendation padding
css = re.sub(
    r'(\.doctor-rec-section\s*\{[^}]*?)padding:\s*42px\s*16px\s*52px\s*16px;',
    r'\1padding: 20px 14px 22px 14px;',
    css
)

# 8. Update Section 9 Offer CTA padding
css = re.sub(
    r'(\.offer-cta-section\s*\{[^}]*?)padding:\s*30px\s*16px\s*56px\s*16px;',
    r'\1padding: 18px 14px 22px 14px;',
    css
)

# 9. Update Section 10 FAQ padding
css = re.sub(
    r'(\.faq-section\s*\{[^}]*?)padding:\s*42px\s*16px\s*54px\s*16px;',
    r'\1padding: 20px 14px 24px 14px;',
    css
)

# Header margins
css = re.sub(
    r'(\.problem-header\s*\{[^}]*?)margin-bottom:\s*26px;',
    r'\1margin-bottom: 16px;',
    css
)

css = re.sub(
    r'(\.product-header\s*\{[^}]*?)margin-bottom:\s*20px;',
    r'\1margin-bottom: 12px;',
    css
)

css = re.sub(
    r'(\.features-top-bar\s*\{[^}]*?)margin-bottom:\s*16px;',
    r'\1margin-bottom: 12px;',
    css
)

css = re.sub(
    r'(\.ingredients-header\s*\{[^}]*?)margin-bottom:\s*24px;',
    r'\1margin-bottom: 16px;',
    css
)

css = re.sub(
    r'(\.quality-header\s*\{[^}]*?)margin-bottom:\s*34px;',
    r'\1margin-bottom: 16px;',
    css
)

css = re.sub(
    r'(\.reviews-header\s*\{[^}]*?)margin-bottom:\s*26px;',
    r'\1margin-bottom: 16px;',
    css
)

css = re.sub(
    r'(\.faq-header\s*\{[^}]*?)margin-bottom:\s*28px;',
    r'\1margin-bottom: 16px;',
    css
)

# Remove extra margin-top from .product-main-title
css = re.sub(
    r'(\.product-main-title\s*\{[^}]*?)margin-top:\s*12px;',
    r'\1margin-top: 0;',
    css
)

with open('css/style.css', 'w', encoding='utf-8') as f:
    f.write(css)

print("Updated style.css with tight, professional paddings & margins!")

# Bump cachebuster in index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=tight_padding_v2', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped cachebuster in index.html to tight_padding_v2!")

