import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(3580, 3645):
    print(f"{i+1}: {lines[i].rstrip()}")
