import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    c = f.read()

c = c.replace('v=clean_trust_spacing_v2', 'v=trust_spacing_perfect_v3')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(c)

print("Bumped cachebuster to trust_spacing_perfect_v3")
