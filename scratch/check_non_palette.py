import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Let's search for yellow, amber, orange, red, green, purple
offending_patterns = [
    r'#FF[0-9A-Fa-f]{4}',
    r'#F0B[0-9A-Fa-f]{3}',
    r'#E58[0-9A-Fa-f]{3}',
    r'#C27[0-9A-Fa-f]{3}',
    r'#FFE[0-9A-Fa-f]{3}',
    r'#FFF6[0-9A-Fa-f]{2}',
    r'gold',
    r'orange',
    r'coral',
    r'amber',
    r'#f59e0b',
    r'#eab308',
    r'#d97706',
    r'#b45309',
    r'#fbbf24',
]

print("Matches in css/style.css:")
for line_no, line in enumerate(css.splitlines(), start=1):
    for pat in offending_patterns:
        if re.search(pat, line, re.IGNORECASE):
            print(f"L{line_no}: {line.strip()}")
            break

print("\nMatches in index.html:")
for line_no, line in enumerate(html.splitlines(), start=1):
    for pat in offending_patterns:
        if re.search(pat, line, re.IGNORECASE):
            print(f"L{line_no}: {line.strip()}")
            break

