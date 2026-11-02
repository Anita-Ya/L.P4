import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print(f"Total lines: {len(lines)}")
for idx in range(max(0, len(lines)-65), len(lines)):
    print(f"{idx+1}: {lines[idx].strip()}")
