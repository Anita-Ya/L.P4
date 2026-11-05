import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

print("FAQ start lines (805-810):")
for j in range(804, 810):
    print(f"{j+1}: {repr(lines[j])}")

print("\nFAQ end & Order start lines (925-937):")
for j in range(924, 937):
    print(f"{j+1}: {repr(lines[j])}")

print("\nOrder end lines (1080-1085):")
for j in range(1079, 1085):
    print(f"{j+1}: {repr(lines[j])}")
