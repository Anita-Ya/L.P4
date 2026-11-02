with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.doctor-bottle-overlay')
print(css[idx:idx+600])

