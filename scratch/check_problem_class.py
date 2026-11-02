with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.problem-detailing-section')
print(css[idx:idx+600])
