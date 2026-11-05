import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'SECTION 10' in line or 'SECTION 11' in line or 'SECTION 12' in line:
        print(f"Line {i+1}: {line.strip()}")
    if '<section class="faq-section"' in line:
        print(f"FAQ start: Line {i+1}")
    if '<section class="order-form-section"' in line:
        print(f"Order start: Line {i+1}")

