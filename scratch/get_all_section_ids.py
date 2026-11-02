import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

sections = re.findall(r'<section[^>]*class=[\'"]([^\'"]*)[\'"][^>]*id=[\'"]([^\'"]*)[\'"]', html)
for cls, sid in sections:
    print(f"ID: #{sid} -> Class: {cls}")

