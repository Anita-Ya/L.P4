import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Remove Problem tag
html = re.sub(r'\s*<div class="problem-tag">.*?</div>', '', html, flags=re.DOTALL)

# 2. Remove Product tag
html = re.sub(r'\s*<div class="product-tag">.*?</div>', '', html, flags=re.DOTALL)

# 3. Clean up features-top-bar in section 4
html = re.sub(r'\s*<!-- Section Header Tag -->\s*<div class="features-top-bar">.*?</div>\s*</div>', '', html, flags=re.DOTALL)

# 4. Remove Ingredients tag
html = re.sub(r'\s*<div class="ingredients-tag">.*?</div>', '', html, flags=re.DOTALL)

# 5. Remove Quality tag
html = re.sub(r'\s*<div class="quality-tag">.*?</div>', '', html, flags=re.DOTALL)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: All section pill tags removed!")

