import re
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find all hex color codes
hex_colors = set(re.findall(r'#[0-9a-fA-F]{3,8}', css))
print("All hex colors in css/style.css:")
for color in sorted(hex_colors):
    print(color)

