with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.offer-top-subtitle')
print(css[idx:idx+400])

