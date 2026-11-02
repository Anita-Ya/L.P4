with open('js/main.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'handleOrderSubmit' in line or 'userPhone' in line or 'userName' in line or 'actualOrderForm' in line:
        print(f"Line {i+1}: {line.strip()}")
        for j in range(max(0, i-5), min(i + 45, len(lines))):
            print(f"{j+1}: {lines[j].rstrip()}")
        break

