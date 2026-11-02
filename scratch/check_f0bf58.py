with open('css/style.css', 'r', encoding='utf-8') as f:
    css = f.read()

idx = css.find('#F0BF58')
print("idx:", idx)
if idx != -1:
    print(css[idx-200:idx+300])

