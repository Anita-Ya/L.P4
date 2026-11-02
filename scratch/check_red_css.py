with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.ayur-input-box')
print(css[idx:idx+800])

