import re

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if any(k in line for k in ['problem-tag', 'product-tag', 'features-tag', 'features-top-bar', 'ingredients-tag', 'quality-tag', 'PROBLEM / PAIN', 'PRODUCT INTRODUCTION', 'SPECIAL FEATURES', 'KEY INGREDIENTS', 'PRODUCT QUALITY & TRUST']):
        print(f"Line {i+1}: {line.strip()}")

