import re

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

matches = re.findall(r'class="[^"]*(?:sticky|float|fixed|bottom)[^"]*"', text, re.I)
print("Matches in index.html:", matches)

with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

fixed_rules = re.findall(r'([.#][\w-]+\s*\{[^}]*position:\s*fixed[^}]*\})', css, re.I)
for r in fixed_rules:
    print("Fixed rule in CSS:\n", r[:200])

