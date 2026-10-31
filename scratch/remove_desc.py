import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Remove the description paragraphs inside the hex cards
html = re.sub(r'\s*<p class="hex-card-desc">.*?</p>', '', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("SUCCESS: removed hex-card-desc!")

