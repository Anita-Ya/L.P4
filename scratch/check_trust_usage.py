import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'order-trust-row' in l:
        for j in range(i-2, min(len(lines), i+30)):
            print(f"{j+1}: {repr(lines[j])}")
        break
