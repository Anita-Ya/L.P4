import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'id="liveOrderToast"' in l:
        for j in range(max(0, i-2), min(i+30, len(lines))):
            print(f"{j+1}: {lines[j].rstrip()}")
        break

