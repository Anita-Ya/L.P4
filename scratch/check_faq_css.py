import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'faq-section' in l or 'faq-header' in l:
        print(f"Line {i+1}: {l.strip()}")
        for j in range(max(0, i-2), min(len(lines), i+25)):
            print(f"  {j+1}: {lines[j].rstrip()}")
        print("="*40)

