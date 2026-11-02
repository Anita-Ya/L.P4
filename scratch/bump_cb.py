import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[^\"]+', 'style.css?v=thankyou_ready_v1', html)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print("Bumped cachebuster to thankyou_ready_v1 in index.html!")

