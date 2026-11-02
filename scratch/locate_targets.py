with open('css/style.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

targets = {'#C27803', '#E58325', '#F0BF58', '#FF5A5F', '#FFB800', '#FFE4B5', '#FFF6E8'}

for i, line in enumerate(lines, start=1):
    for t in targets:
        if t.lower() in line.lower():
            print(f"Line {i}: {line.strip()}")

