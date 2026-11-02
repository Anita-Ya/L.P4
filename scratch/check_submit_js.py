import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

idx = js.find('function handleOrderSubmit')
print(js[idx:])

