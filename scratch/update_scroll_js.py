import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

target = "const orderSection = document.getElementById('order') || document.querySelector('.ayur-order-card');"
replacement = "const orderSection = document.getElementById('orderForm') || document.getElementById('order') || document.querySelector('.ayur-order-card');"

if target in js:
    js = js.replace(target, replacement)
    with open('js/main.js', 'w', encoding='utf-8') as f:
        f.write(js)
    print("js/main.js updated!")
else:
    print("Target not found in js/main.js")

