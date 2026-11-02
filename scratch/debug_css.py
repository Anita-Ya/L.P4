with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    if 'ayur-field-group' in l:
        for j in range(max(0, i-2), min(i+35, len(lines))):
            print(f"{j+1}: {repr(lines[j])}")
        break

