import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

print("CTAs found:")
for m in re.finditer(r'href=[\'"][^\'"]*[\'"]', html):
    print(m.group(0))

print("\nForm or order IDs:")
for m in re.finditer(r'id=[\'"][^\'"]*[\'"]', html):
    print(m.group(0))

