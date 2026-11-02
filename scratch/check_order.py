import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'id="order"' in line or 'id=\'order\'' in line or 'class="order-section"' in line or 'ayur-order-card' in line:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(i, min(i + 50, len(lines))):
            print(f"{j+1}: {lines[j].rstrip()}")
        break

