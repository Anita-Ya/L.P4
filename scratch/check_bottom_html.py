with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[-70:]):
    print(f"{len(lines)-70+i+1}: {l.rstrip()}")

