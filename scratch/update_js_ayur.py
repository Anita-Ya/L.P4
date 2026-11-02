with open('js/main.js', 'r', encoding='utf-8') as f:
    js = f.read()

js = js.replace('.ref-order-card', '.ayur-order-card')
js = js.replace("submitBtn.style.background = '#28a745';", "submitBtn.style.background = '#33C3A5';")

with open('js/main.js', 'w', encoding='utf-8') as f:
    f.write(js)

print("Updated js/main.js!")

