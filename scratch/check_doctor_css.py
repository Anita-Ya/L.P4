with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('.doctor-rec-section')
print(css[idx:idx+1500])

