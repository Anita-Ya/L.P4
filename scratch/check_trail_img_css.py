with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.trail-circle-img')
print(css[idx-100:idx+600])

