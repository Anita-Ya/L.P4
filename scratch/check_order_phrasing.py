import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

for line in text.splitlines():
    if 'ऑर्डर दिया' in line or 'ऑर्डर किया' in line:
        print("In index.html:", line)

with open('js/main.js', 'r', encoding='utf-8') as f:
    text_js = f.read()

for line in text_js.splitlines():
    if 'ऑर्डर दिया' in line or 'ऑर्डर किया' in line:
        print("In js/main.js:", line)

