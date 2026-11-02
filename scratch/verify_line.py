import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'toast-product-action' in l:
        print(f"{i+1}: {lines[i].rstrip()}")
        print(f"{i+2}: {lines[i+1].rstrip()}")
        print(f"{i+3}: {lines[i+2].rstrip()}")

