import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if '<section' in l or '</section>' in l or '<footer' in l or '</footer' in l:
        if i > 790:
            print(f"Line {i+1}: {l.strip()[:80]}")
