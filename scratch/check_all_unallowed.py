with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re

# Let's find all hex colors in the entire file that are NOT in our palette
allowed_navies = {'#0b3c5d', '#07253b', '#062338', '#041726', '#051f33', '#061623', '#071927', '#08121d', '#0c4e6d', '#0d2338', '#111e2e'}
allowed_mints = {'#33c3a5', '#28ac91', '#2cb296', '#0e7461', '#6ee7b7'}
allowed_ice_blues = {'#f2f8fb', '#edf4f7', '#edf6f3', '#eef3f6', '#f4f8fa', '#f5f9fa', '#f5faf9', '#f5fafa', '#f8fbfc', '#f7fafc', '#f8fbfb', '#e2f2ee', '#f4faf8', '#ebf3f7', '#d6e4ee', '#e2edf8', '#e1edf4', '#e2ecf2', '#eaf1f5', '#d3e7f2', '#d5e4ec', '#d5e7f2'}
allowed_whites = {'#ffffff', '#fff'}
allowed_neutrals_text = {'#1e293b', '#2c3e50', '#2f4e64', '#334155', '#4a6072', '#4a6b82', '#6c8294', '#7a8e9e', '#7b8f9e', '#8a9ca8', '#8c9ca8', '#8c9ea8', '#a0b2c0', '#a0c2d6', '#c0d6e4'}

all_allowed = allowed_navies | allowed_mints | allowed_ice_blues | allowed_whites | allowed_neutrals_text

hexes = re.findall(r'#[0-9a-fA-F]{3,8}', css)
unallowed = set()
for h in hexes:
    if h.lower() not in all_allowed:
        unallowed.add(h)

print("Non-palette hexes found in style.css:")
for u in sorted(unallowed):
    print(u)

