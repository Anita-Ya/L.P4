import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Find all hex colors in index.html
hexes = set(re.findall(r'#[0-9a-fA-F]{3,8}', html))
print("All hex codes in index.html:")
for h in sorted(hexes):
    print(h)

# Find any color attributes in SVGs or inline styles
for line_no, line in enumerate(html.splitlines(), start=1):
    if any(k in line.lower() for k in ['stroke="', 'fill="', 'style="']):
        print(f"L{line_no}: {line.strip()[:80]}")

